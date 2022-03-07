# Program to implement a Round Robin CPU scheduling algorithm

print("Round Robin scheduling Algorithm")
print("================================\n")

headers = ['Processes','Burst Time','Waiting Time'
            ,'Turn-Around Time']

# Storing output as a list
out = []

# Storing given value of quantum time
quantum = 2 

# Get number of processes
N = int(input('Enter number of processes :: '))

bt = [] # Going to store the burst times in this to use them without modifying the original values
t = 0 # Store time

# Get Burst times for each process
for i in range(0,N):
    k = f"P{i+1}"
    b = int(input(f"Enter Burst time of process{i+1} :: "))

    out.append([k,[b]])
    bt.append(b)

# Calculating Waiting times
while True:
    done = True
    for i in range(0,N):
        if bt[i] > 0:
            done = False
            if(bt[i] > quantum):
                t += quantum
                bt[i] -= quantum
            else:
                t += bt[i]
                out[i][1].append(t-out[i][1][0])
                bt[i] = 0
    if done == True:
        break

# Calculating turn around times
for i in range(0,N):
    out[i][1].append(out[i][1][0] + out[i][1][1])

avgWT = 0
avgTAT = 0

for i in range(0,N):
    avgWT += out[i][1][1]
    avgTAT += out[i][1][2]

avgWT /= N
avgTAT /= N

print(f"\n Quantum := {quantum}")
print(f"\n{headers[0]:^15}{headers[1]:^15}{headers[2]:^15}{headers[3]:^15}")
for a in out:
    print(f"{a[0]:^15}{a[1][0]:^15}{a[1][1]:^15}{a[1][2]:^15}")
print(f"\nAverage Waiting Time : {avgWT:.2f} ns \nAverage Turn-Around Time : {avgTAT:.2f} ns")