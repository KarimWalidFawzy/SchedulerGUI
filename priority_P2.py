class Process:

    finish_time = None
    turn_around_time = None
    waiting_time = None

    def __init__(self, name, arrival_time, burst_time, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        
        
        
        
class Scheduler:        
    
    
    def schedule():
        processes = []
        scheduler = []
        memory = []
        time = 0
        
        #taking number of processes
        NumberOfProcesses = int(input("Enter number of processes: "))

        #taking processes info
        for process in range(NumberOfProcesses):
            name = input("Enter name of process: ")
            arr = int(input("Enter arrival time: "))
            bur = int(input("Enter burst time: "))
            prio = int(input("Enter priority: "))
            
            #adding all processes to processes list
            processes.append(Process(name,arr,bur,prio))

            #sorting by arrival time
            processes = sorted(processes, key = lambda process : process.arrival_time)
        
            
        bursts = []
        for i in processes:
            bursts.append(i.burst_time)
            
            
        #Main Logic
        #adding existing processes till now
        for process in processes :
            if process.arrival_time == processes[0].arrival_time :
                memory.append(process)


        #checking highest priority value
        while len(memory) != 0 :
            HighestPriority = 99
            for process in memory :
                if process.priority < HighestPriority :
                    HighestPriority = process.priority
            
            for i in range(len(memory)) :
                if memory[i].priority == HighestPriority :
                    scheduler.append(memory[i].name)
                    memory[i].burst_time = memory[i].burst_time - 1
                    break
            
            
                
            #updating time
            time = time + 1
            
            #adding arrived processes
            for process in processes :
                if process.arrival_time == time :
                    memory.append(process)
            
            #removing finished processes
            for item in memory[:] :
                if item.burst_time == 0 :
                    item.finish_time = time
                    memory.remove(item)

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





Scheduler.schedule()