# QUESTION 7
# LAB-7: FIFO PAGE REPLACEMENT ALGORITHM

print("===========================================")
print("       FIFO Page Replacement Algorithm")
print("===========================================")

pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frame_size = 3

frames = []
page_faults = 0

print("{:<8}{:<20}{:<15}".format("Page", "Frames", "Status"))
print("-" * 45)

for page in pages:
    if page not in frames:
        page_faults += 1

        if len(frames) < frame_size:
            frames.append(page)
        else:
            frames.pop(0)
            frames.append(page)

        status = "Page Fault"
    else:
        status = "Hit"

    print("{:<8}{:<20}{:<15}".format(page, str(frames), status))

print("-" * 45)
print("Total Page Faults =", page_faults)
