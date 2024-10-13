Basic Adaptive Cruise Control (ACC) Implementation

This repository contains a simplified implementation of an Adaptive Cruise Control (ACC) system, developed using Python. The goal of this project is to demonstrate the core principles of ACC and provide an educational tool for learning about this essential automotive technology.

Project Overview

This ACC system uses a PID controller to adjust the vehicle’s throttle and maintain a target speed set by the driver. The system interacts with speed sensors and throttle control to dynamically match the vehicle’s current speed with the desired target speed.

Key components include:

	•	Driver Inputs: Set or adjust the target speed using the dashboard.
	•	PID Controller: Adjusts the throttle based on the error between the current speed and the target speed.
	•	Vehicle Control: Includes throttle and speed sensor systems.
	•	Interactive Dashboard: Provides a user interface to visualize the speed data and control inputs.

Architecture

The project’s architecture is modeled using PlantUML, and the corresponding architecture diagram can be found in the repository. The implementation is broken down into modular Python scripts:

	•	car.py: Handles throttle control and speed sensor simulation.
	•	cruise_control_app.py: Provides the interactive dashboard for driver inputs.
	•	main.py: Runs the entire ACC system.
	•	pid_controller.py: Implements the PID controller logic for speed adjustments.
	•	basic_acc_architecture.puml / BasicACCArchitecture.png: Contains the UML diagram of the system’s architecture.


Usage

1- Clone the repository

git clone https://github.com/HamzaELHANBALI/basic_acc

2- Navigate to the project directory

cd basic_acc

3- Install the required Python dependencies 

pip install -r requirements.txt

4- Run the main Python file

python main.py