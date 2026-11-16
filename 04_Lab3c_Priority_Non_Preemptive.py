# QUESTION 4
# LAB-3(c): PRIORITY SCHEDULING - NON-PREEMPTIVE

n = int(input("Enter number of processes: "))
at = []
bt = []
pr = []

for i in range(n):
    at.append(int(input("Arrival time: ")))
    bt.append(int(input("Burst time: ")))
    pr.append(int(input("Priority: ")))

done = [0] * n
ct = [0] * n
time = 0
count = 0

while count < n:
    available = [i for i in range(n) if at[i] <= time and done[i] == 0]

    if not available:
        time += 1
        continue

    # Smaller priority number means higher priority in this lab program.
    i = min(available, key=lambda x: pr[x])
    time += bt[i]
    ct[i] = time
    done[i] = 1
    count += 1

print("Process CT TAT WT")
for i in range(n):
    tat = ct[i] - at[i]
    wt = tat - bt[i]
    print(i + 1, ct[i], tat, wt)
