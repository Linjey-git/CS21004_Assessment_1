# CPU Scheduling Algorithms Simulator

This project is a Python-based simulator for demonstrating various CPU scheduling algorithms, including:
- **First In, First Out (FIFO)**, also known as **First-Come-First-Served (FCFS)**
- **Shortest Job First (SJF)**
- **Shortest Time-to-Completion First (STCF)**
- **Round-Robin (RR)**

## Project Overview

This project was developed as part of a university assignment to understand and analyze different CPU scheduling algorithms. The simulator provides insights into how these algorithms work and allows for a comparison of their efficiency based on response time, turnaround time, and CPU utilization. Users can input process details and choose a scheduling algorithm to observe how the processes are managed in a simulated CPU environment.

### Features
- **Multiple Scheduling Algorithms:** The program supports FIFO, SJF, STCF, and RR, allowing users to switch between these methods and observe their effects.
- **Detailed Process Tracking:** Each process's completion time, response time, turnaround time, and waiting time are calculated and displayed.
- **CPU Utilization Calculation:** The program tracks CPU utilization to evaluate the efficiency of each algorithm.
- **Input Validation:** User input is validated to ensure accuracy, with checks in place to handle invalid entries.

## How It Works

1. **User Input:** The user is prompted to enter the number of processes, along with their IDs, arrival times, and burst times. The user then selects the scheduling algorithm they want to use.
2. **Process Simulation:** The selected algorithm is applied to the list of processes, calculating the necessary statistics for each one.
3. **Statistics Display:** After the simulation, the program displays a summary of all the processes, including:
   - Completion time
   - Turnaround time
   - Waiting time
   - Response time
4. **Algorithm Comparison:** It provides an average of the turnaround, waiting, and response times, along with the CPU utilization rate for the chosen scheduling method.

## Technologies Used
- **Programming Language:** Python 3
- **Concepts:** Process scheduling, queue management, CPU utilization

## Requirements
- Python 3.x installed on your system

