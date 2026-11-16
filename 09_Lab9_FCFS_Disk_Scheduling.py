# QUESTION 9
# LAB-9: FCFS DISK SCHEDULING ALGORITHM

head = 53
requests = [98, 183, 37, 122, 14, 124, 65, 67]
seek_time_per_track = 0.1

total_head_movement = 0
current_head = head

print("FCFS Disk Scheduling Algorithm")
print("Initial Head Position:", head)
print("Request Sequence:", requests)
print("\nHead Movement:")

for request in requests:
    movement = abs(current_head - request)
    total_head_movement += movement
    print(f"{current_head} -> {request}: {movement} tracks")
    current_head = request

total_seek_time = total_head_movement * seek_time_per_track

print("\nTotal Head Movement:", total_head_movement, "tracks")
print("Total Seek Time:", round(total_seek_time, 2), "ms")
