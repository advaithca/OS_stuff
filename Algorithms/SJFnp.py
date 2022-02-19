print("Shortest Job First Algorithm")
print("============================\n")

headers = ['Processes','Arrival Time','Burst Time','Waiting Time'
            ,'Turn-Around Time','Completion Time']

# Dictionary to store the output
out = dict()

# Get number of processes from User
N = int(input("Number of processes : "))

a, b = 0, 0
# Get Arrival time and Burst time of N processes
for i in range(0,N):
    k = f"P{i+1}"
    a = int(input(f"Enter Arrival time of process{i+1} :: "))
    b = int(input(f"Enter Burst time of process{i+1} :: "))
    out[k] = [a,b]

# storing processes in order of increasing arrival time
out = sorted(out.items(),key=lambda i:i[1][0])
readyQ = [x for x in out[1:]]

# Storing ready queue in order of increasing Burst Times
readyQ.sort(key=lambda i:i[1][1])

# Setting completion time of first process as its burst time
out[0][1].append(out[0][1][1])

# Calculating Completion times of rest of the processes
for i in range(0,len(readyQ)):
    if i == 0:
        readyQ[i][1].append(readyQ[i][1][1] + out[0][1][2])
    else:
        readyQ[i][1].append(readyQ[i][1][1] + readyQ[i-1][1][2])

out.sort(key=lambda i:i[0])

# Storing turn around times
for i in range(0,N):
    out[i][1].append(out[i][1][2]-out[i][1][0])

# Storing waiting times
for i in range(0,N):
    out[i][1].append(out[i][1][3]-out[i][1][1])

# storing avg waiting time and avg turn around time
avgWaitTime = 0
avgTATime = 0
for i in range(0,N):
    avgWaitTime += out[i][1][4]
    avgTATime += out[i][1][3]

avgWaitTime /= N
avgTATime /= N

print(f"\n{headers[0]:^15}{headers[1]:^15}{headers[2]:^15}{headers[3]:^15}{headers[4]:^20}{headers[5]:^20}")
for a in out:
    print(f"{a[0]:^15}{a[1][0]:^15}{a[1][1]:^15}{a[1][4]:^15}{a[1][3]:^20}{a[1][2]:^20}")
print(f"\nAverage Waiting Time : {avgWaitTime}\nAverage Turn-Around Time : {avgTATime}")