# QUESTION 3
# LAB-3(b): SHORTEST JOB FIRST (SJF) - NON-PREEMPTIVE CPU SCHEDULING

n = int(input("Enter number of processes: "))
at = []
bt = []

for i in range(n):
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))

done = [0] * n
ct = [0] * n
time = 0
count = 0

while count < n:
    available = [i for i in range(n) if at[i] <= time and done[i] == 0]

    if not available:
        time += 1
        continue

    i = min(available, key=lambda x: bt[x])
    time += bt[i]
    ct[i] = time
    done[i] = 1
    count += 1

print("Process CT TAT WT")
for i in range(n):
    tat = ct[i] - at[i]
    wt = tat - bt[i]
    print(i + 1, ct[i], tat, wt)
