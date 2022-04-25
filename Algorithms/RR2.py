#Program to implement Round Robin
print("Round Robin Scheduling algorithm")
print("================================")

headers = ['Processes','Arrival Time','Burst Time','Completion Time','Waiting Time',
           'Turn-Around Time']

out = []

quantum = int(input("Enter value for quantum := "))

N = int(input("Enter number of processes := "))

bt = []
t = 0

for i in range(N):
    k = f'P{i+1}'
    a = int(input(f"Enter arrival time of process {k} := "))
    b = int(input(f"Enter burst time of process {k} := "))
    out.append([k,[a,b,0,0,0],0])
    bt.append(b)

while True:
    done = True
    for i in range(N):
        if bt[i] > 0:
            done = False
        if bt[i] > quantum:
            t += quantum
            bt[i] -= quantum
        else:
            if out[i][2] != 1:
                t += bt[i]
                out[i][1][2] += t - out[i][1][1] - out[i][1][0]
                bt[i] = 0
                out[i][2] = 1
    if done == True:
        break

for i in range(N):
    out[i][1][3] = out[i][1][1] + out[i][1][2]

for i in range(N):
    out[i][1][4] = out[i][1][3] + out[i][1][0]

avgWT = 0
avgTAT = 0

for i in range(N):
    avgWT += out[i][1][2]
    avgTAT += out[i][1][3]

avgWT /= N
avgTAT /= N

print(f"{headers[0]:^15}{headers[1]:^15}{headers[2]:^15}{headers[3]:^15}{headers[4]:^15}{headers[5]:^15}")
for a in out:
   print(f"{a[0]:^15}{a[1][0]:^15}{a[1][1]:^15}{a[1][4]:^15}{a[1][2]:^15}{a[1][3]:^15}")

print(f"Average Waiting Time : {avgWT}\nAverage Turn-Around time : {avgTAT}")
