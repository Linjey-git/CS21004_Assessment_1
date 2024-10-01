class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0
        self.remaining_time = burst_time

def get_process_info():
    processes = []
    processes_amount = int(input("Enter the number of processes: "))
    for i in range(processes_amount):
        pid = input(f"Enter Process ID for process {i+1}: ")
        arrival_time = int(input(f"Enter arrival time for process {pid}: "))
        burst_time = int(input(f"Enter burst time for process {pid}: "))
        processes.append(Process(pid, arrival_time, burst_time))
    return processes


def fifo_scheduling(processes):
    time = 0
    for process in processes:
        if time < process.arrival_time:
            time = process.arrival_time
        process.waiting_time = time - process.arrival_time
        process.completion_time = time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        time = process.completion_time


def round_robin_scheduling(processes, quantum):
    time = 0
    queue = processes[:]
    while queue:
        process = queue.pop(0)
        if process.remaining_time > quantum:
            time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:
            time += process.remaining_time
            process.remaining_time = 0
            process.completion_time = time
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time


def display_statistics(processes):
    total_turnaround = 0
    total_waiting = 0
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        total_turnaround += process.turnaround_time
        total_waiting += process.waiting_time
        print(
            f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

    processes_amount = len(processes)
    print(f"Average Turnaround Time: {total_turnaround / processes_amount}")
    print(f"Average Waiting Time: {total_waiting / processes_amount}")


def main():
    processes = get_process_info()
    algo_choice = input("Select scheduling algorithm (FIFO/RR): ").lower()

    if algo_choice == "fifo":
        fifo_scheduling(processes)
    elif algo_choice == "rr":
        quantum = int(input("Enter time quantum for Round Robin: "))
        round_robin_scheduling(processes, quantum)

    display_statistics(processes)


if __name__ == "__main__":
    main()
