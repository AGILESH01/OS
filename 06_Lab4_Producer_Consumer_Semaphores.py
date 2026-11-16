# QUESTION 6
# LAB-4: PRODUCER-CONSUMER PROBLEM USING SEMAPHORES

import threading
import time

buffer = []
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Lock()

def producer():
    for i in range(1, 6):
        empty.acquire()
        mutex.acquire()

        buffer.append(i)
        print("Produced:", i)

        mutex.release()
        full.release()
        time.sleep(1)

def consumer():
    for i in range(1, 6):
        full.acquire()
        mutex.acquire()

        item = buffer.pop(0)
        print("Consumed:", item)

        mutex.release()
        empty.release()
        time.sleep(1)

t1 = threading.Thread(target=producer)
t2 = threading.Thread(target=consumer)

t1.start()
t2.start()

t1.join()
t2.join()

print("Production and consumption completed")
