class Process:
    finish_time = None
    turn_around_time = None
    waiting_time = None

    def __init__(self, name, arrival_time, burst_time, priority=None):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority


class Scheduler:
    # First Come First Serve
    def FCFS(self):
        processes = []
        scheduler = []

        # taking number of processes
        NumberOfProcesses = int(input("Enter number of processes: "))

        # taking processes info
        for process in range(NumberOfProcesses):
            name = input("Enter name of process: ")
            arr = int(input("Enter arrival time: "))
            bur = int(input("Enter burst time: "))

            # adding all processes to processes list
            processes.append(Process(name, arr, bur))

        # Sorting by arrival time
        processes = sorted(processes, key=lambda process: process.arrival_time)

        # Main logic
        time = processes[0].arrival_time
        for process in processes:
            curr_process = [process.name, time, time + process.burst_time]
            scheduler.append(curr_process)
            time += process.burst_time
            process.finish_time = time

        # Calculate turnaround time and waiting time
        total_turnaround_time = 0
        total_waiting_time = 0
        for process in processes:
            process.turn_around_time = process.finish_time - process.arrival_time
            process.waiting_time = process.turn_around_time - process.burst_time
            total_turnaround_time += process.turn_around_time
            total_waiting_time += process.waiting_time

        # Calculate averages
        avg_turnaround_time = total_turnaround_time / NumberOfProcesses
        avg_waiting_time = total_waiting_time / NumberOfProcesses

        print("Scheduler:", scheduler)
        print("Average Waiting Time =", avg_waiting_time)
        print("Average Turnaround Time =", avg_turnaround_time)

        for i, process in enumerate(processes):
            print("Waiting time for", process.name, "=", process.waiting_time)

    # Shortest Job First Non-Preemptive
    def SJF_NP(self):
        processes = []
        scheduler = []
        memory = []

        # taking number of processes
        NumberOfProcesses = int(input("Enter number of processes: "))

        # taking processes info
        for process in range(NumberOfProcesses):
            name = input("Enter name of process: ")
            arr = int(input("Enter arrival time: "))
            bur = int(input("Enter burst time: "))

            # adding all processes to processes list
            processes.append(Process(name, arr, bur))

        remaining_processes = list(processes)
        time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time

        # Main Logic
        while len(remaining_processes) != 0:
            # Take all processes whose arrival time is less than time
            for process in remaining_processes:
                if process.arrival_time <= time:
                    memory.append(process)

            # If there is no processes in memory but there is still processes in remaining_processes
            if len(memory) == 0:
                time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time

            # Finish all processes in memory
            while len(memory) != 0:
                shortest_job = min(memory, key=lambda x: x.burst_time)
                curr_process = [shortest_job.name, time, time + shortest_job.burst_time]
                scheduler.append(curr_process)
                time += shortest_job.burst_time
                shortest_job.finish_time = time
                memory.remove(shortest_job)
                remaining_processes.remove(shortest_job)

        # Calculate turnaround time and waiting time
        total_turnaround_time = 0
        total_waiting_time = 0
        for process in processes:
            process.turn_around_time = process.finish_time - process.arrival_time
            process.waiting_time = process.turn_around_time - process.burst_time
            total_turnaround_time += process.turn_around_time
            total_waiting_time += process.waiting_time

        # Calculate averages
        avg_turnaround_time = total_turnaround_time / NumberOfProcesses
        avg_waiting_time = total_waiting_time / NumberOfProcesses

        print("Scheduler:", scheduler)
        print("Average Waiting Time =", avg_waiting_time)
        print("Average Turnaround Time =", avg_turnaround_time)

        for i, process in enumerate(processes):
            print("Waiting time for", process.name, "=", process.waiting_time)

    # Priority Preemptive
    def Priority_P(self):
        processes = []
        scheduler = []
        memory = []

        # taking number of processes
        NumberOfProcesses = int(input("Enter number of processes: "))

        # taking processes info
        for process in range(NumberOfProcesses):
            name = input("Enter name of process: ")
            arr = int(input("Enter arrival time: "))
            bur = int(input("Enter burst time: "))
            prio = int(input("Enter priority: "))

            # adding all processes to processes list
            processes.append(Process(name, arr, bur, prio))

        remaining_processes = list(processes)
        time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time

        # Main Logic
        # adding existing processes till now
        while len(remaining_processes) != 0:
            for process in remaining_processes:
                if process.arrival_time <= time:
                    memory.append(process)

            # If there is no processes in memory but there is still processes in remaining_processes
            if len(memory) == 0:
                time = min(remaining_processes, key=lambda x: x.arrival_time).arrival_time

            # checking the highest priority value
            while len(memory) != 0:
                HighestPriority = min(memory, key=lambda x: x.priority)
                curr_process = [HighestPriority.name, time, time+1]
                scheduler.append(curr_process)
                HighestPriority.burst_time -= 1

                # updating time
                time = time + 1

                # removing finished processes
                if HighestPriority.burst_time == 0:
                    HighestPriority.finish_time = time
                    memory.remove(HighestPriority)
                    remaining_processes.remove(HighestPriority)

                # adding arrived processes
                for process in processes:
                    if process.arrival_time == time:
                        memory.append(process)

        # Calculate turnaround time and waiting time
        total_turnaround_time = 0
        total_waiting_time = 0
        for process in processes:
            process.turn_around_time = process.finish_time - process.arrival_time
            process.waiting_time = process.turn_around_time - process.burst_time
            total_turnaround_time += process.turn_around_time
            total_waiting_time += process.waiting_time

        # Calculate averages
        avg_turnaround_time = total_turnaround_time / NumberOfProcesses
        avg_waiting_time = total_waiting_time / NumberOfProcesses

        print("Scheduler:", scheduler)
        print("Average Waiting Time =", avg_waiting_time)
        print("Average Turnaround Time =", avg_turnaround_time)

        for i, process in enumerate(processes):
            print("Waiting time for", process.name, "=", process.waiting_time)
