# QUESTION 2
# LAB-3(a): FIRST COME FIRST SERVED (FCFS) CPU SCHEDULING

n = int(input("Enter number of processes: "))
at = []
bt = []

for i in range(n):
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))

time = 0
ct = []

# Processes are executed in the order entered (as in the lab question).
for i in range(n):
    time = max(time, at[i]) + bt[i]
    ct.append(time)

print("Process CT TAT WT")
for i in range(n):
    tat = ct[i] - at[i]
    wt = tat - bt[i]
    print(i + 1, ct[i], tat, wt)
