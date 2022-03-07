# Program to implement Round Robin CPU scheduling algorithm

print("Round Robin scheduling Algorithm")
print("================================\n")

headers = ['Processes','Arrival Time','Burst Time','Waiting Time'
            ,'Turn-Around Time']

readyQ = []
quantum = 2
# list to store the output
out = []

# Get number of processes from User
N = int(input("Number of processes : "))

a, b = 0, 0
t = 0
T = 0
# Get Arrival time and Burst time of N processes
for i in range(0,N):
    k = f"P{i+1}"
    a = int(input(f"Enter Arrival time of process{i+1} :: "))
    b = int(input(f"Enter Burst time of process{i+1} :: "))

    out.append([k,[a,b,b,0,0],0])
    t += b

# Sort in order of arrival times
out = sorted(out, key=lambda i : i[1][0])

while t != 0:
    for i in range(0,len(out)):
        if out[i][1][2] <= quantum and out[i][1][2] >= 0:
            T += out[i][1][2]
            t -= out[i][1][2]
            out[i][1][2] = 0 
        elif out[i][1][2] > 0:
            out[i][1][2] -= quantum
            t -= quantum
            T += quantum
        if out[i][1][2] == 0 and out[i][2] != 1:
            out[i][1][3] += T - (out[i][1][0] + out[i][1][1])
            out[i][1][4] += T - out[i][1][0]
            out[i][2] = 1

# storing avg waiting time and avg turn around time
avgWaitTime = 0
avgTATime = 0
for i in range(0,N):
    avgWaitTime += out[i][1][3]
    avgTATime += out[i][1][4]

avgWaitTime /= N
avgTATime /= N

print(f"\n{headers[0]:^15}{headers[1]:^15}{headers[2]:^15}{headers[3]:^15}{headers[4]:^20}")
for a in out:
    print(f"{a[0]:^15}{a[1][0]:^15}{a[1][1]:^15}{a[1][3]:^15}{a[1][4]:^20}")
print(f"\nAverage Waiting Time : {avgWaitTime:.2f}\nAverage Turn-Around Time : {avgTATime:.2f}")