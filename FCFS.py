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

# storing Completion times
for i in range(0,N):
    if i==0:
        out[i][1].append(out[i][1][1])
    else:
        out[i][1].append(out[i-1][1][2]+out[i][1][1])

# storing turn-around times
for i in range(0,N):
    out[i][1].append(out[i][1][2]-out[i][1][0])

# storing waiting time
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

print(f"{headers[0]:12} {headers[1]:12} {headers[2]:12} {headers[3]:12} {headers[4]:12} {headers[5]:12}")
for a in out:
    print(f"{a}")