import threading
import time
import random
global_counter = 0
binary_semaphore = threading.Lock()
NUM_WORKERS = 5
def worker(worker_id):
    global global_counter
    
    print(f"Worker-{worker_id}: requesting binary semaphore")
    binary_semaphore.acquire()
    start_time = time.time( )
    global_counter = 1
    print (f"Worker - {worker_id} : global_counter = {global_counter} (inside critical section)")
    work_time = random. uniform(1, 3)
    print(f"Worker-{worker_id}: working in critical section  {work_time :.2f} seconds ")
    time.sleep(work_time)
    elapsed = time.time() - start_time
    print(f"Worker-{worker_id}: spent {elapsed :.2f} seconds in critical section")
    global_counter = 0
    print(f"Worker-{worker_id}: global_counter ={global_counter}(leaving critical section)")
    binary_semaphore.release()
    print(f"Worker-{worker_id}: released binary semaphore\n")
threads = []
for i in range(NUM_WORKERS):
    t = threading. Thread(target=worker, args=(i+1,))
    threads. append(t)
    t.start()
for t in threads:
    t.join()
print(f"\nAll workers finished. Global counter = {global_counter}")
