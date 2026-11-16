# QUESTION 5
# LAB-3(d): ROUND ROBIN CPU SCHEDULING
# This lab version assumes all processes arrive at time 0.

n = int(input("Enter number of processes: "))
bt = []

for i in range(n):
    bt.append(int(input("Burst time: ")))

q = int(input("Enter time quantum: "))
rem = bt.copy()
ct = [0] * n
time = 0

while any(rem):
    for i in range(n):
        if rem[i] > 0:
            x = min(q, rem[i])
            time += x
            rem[i] -= x

            if rem[i] == 0:
                ct[i] = time

print("Process CT TAT WT")
for i in range(n):
    tat = ct[i]
    wt = tat - bt[i]
    print(i + 1, ct[i], tat, wt)
