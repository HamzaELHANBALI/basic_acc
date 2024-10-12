import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

class PIDController:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.previous_error = 0
        self.integral = 0

    def compute(self, error, dt):
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        self.previous_error = error
        return output

class Car:
    def __init__(self, target_speed):
        self.speed = 0
        self.target_speed = target_speed
        self.pid = PIDController(kp=0.5, ki=0, kd=0)

    def update_speed(self, dt):
        error = self.target_speed - self.speed
        acceleration = self.pid.compute(error, dt)
        self.speed += acceleration * dt
        self.speed = max(0, min(self.speed, 100))  # Limit speed between 0 and 100 mph
        return self.speed

class CruiseControlApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cruise Control Simulation")
        self.geometry("800x600")

        self.car = Car(target_speed=60)
        self.speed_history = []
        self.target_speed_history = []
        self.time_history = []
        self.time_step = 0.1  # 100ms
        self.start_time = time.time()

        self.create_widgets()

    def create_widgets(self):
        # Speed display
        self.speed_label = ctk.CTkLabel(self, text="Current Speed: 0 mph", font=("Arial", 24))
        self.speed_label.pack(pady=10)

        # Target speed display and buttons
        target_speed_frame = ctk.CTkFrame(self)
        target_speed_frame.pack(pady=10)

        self.set_minus_button = ctk.CTkButton(target_speed_frame, text="Set-", command=self.decrease_target_speed, width=60)
        self.set_minus_button.pack(side=ctk.LEFT, padx=5)

        self.target_speed_label = ctk.CTkLabel(target_speed_frame, text="Target Speed: 60 mph", width=150)
        self.target_speed_label.pack(side=ctk.LEFT, padx=5)

        self.set_plus_button = ctk.CTkButton(target_speed_frame, text="Set+", command=self.increase_target_speed, width=60)
        self.set_plus_button.pack(side=ctk.LEFT, padx=5)

        # Start/Stop button
        self.toggle_button = ctk.CTkButton(self, text="Start", command=self.toggle_simulation)
        self.toggle_button.pack(pady=10)

        # Matplotlib figure
        self.figure, self.ax = plt.subplots(figsize=(7, 4))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(fill=ctk.BOTH, expand=True)

        self.speed_line, = self.ax.plot([], [], label='Current Speed')
        self.target_line, = self.ax.plot([], [], label='Target Speed', linestyle='--')
        self.ax.set_ylim(0, 100)
        self.ax.set_xlim(0, 60)  # Show 60 seconds of data
        self.ax.set_xlabel('Time (s)')
        self.ax.set_ylabel('Speed (mph)')
        self.ax.set_title('Speed vs Time')
        self.ax.legend()

        self.running = False

    def increase_target_speed(self):
        self.car.target_speed = min(100, self.car.target_speed + 1)
        self.update_target_speed_label()

    def decrease_target_speed(self):
        self.car.target_speed = max(0, self.car.target_speed - 1)
        self.update_target_speed_label()

    def update_target_speed_label(self):
        self.target_speed_label.configure(text=f"Target Speed: {self.car.target_speed} mph")

    def toggle_simulation(self):
        if self.running:
            self.running = False
            self.toggle_button.configure(text="Start")
        else:
            self.running = True
            self.toggle_button.configure(text="Stop")
            self.start_time = time.time()
            self.run_simulation()

    def run_simulation(self):
        if self.running:
            current_time = time.time() - self.start_time
            current_speed = self.car.update_speed(self.time_step)
            
            self.speed_history.append(current_speed)
            self.target_speed_history.append(self.car.target_speed)
            self.time_history.append(current_time)

            self.speed_label.configure(text=f"Current Speed: {current_speed:.1f} mph")
            self.update_graph()

            self.after(int(self.time_step * 1000), self.run_simulation)

    def update_graph(self):
        self.speed_line.set_data(self.time_history, self.speed_history)
        self.target_line.set_data(self.time_history, self.target_speed_history)
        
        if self.time_history[-1] > 60:
            self.ax.set_xlim(self.time_history[-1] - 60, self.time_history[-1])
        
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

if __name__ == "__main__":
    app = CruiseControlApp()
    app.mainloop()
