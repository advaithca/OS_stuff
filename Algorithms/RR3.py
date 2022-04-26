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

out.sort(key=lambda i: i[1][1], reverse=True)
bt = [x[1][1] for x in out]

readyQ = []

while t <= sum(bt):
    for i in range(N):
        if out[i][1][0] <= t:
            readyQ.append([out[i],i])
    if readyQ:
        for i in range(len(readyQ)):
            a = readyQ.pop(0)
            if a[0][1][1] > 0 and a[0][1][1] > quantum:
                a[0][1][1] -= quantum
                t += quantum
                readyQ.append(a)
            elif a[0][1][1] <= quantum:
                t += a[0][1][1]
                a[0][1][1] = 0
                out[a[1]][1][2] = t

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
