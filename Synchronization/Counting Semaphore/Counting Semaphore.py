import threading
import time
import random

MAX_CS = 3
count_sem = threading.Semaphore(MAX_CS)
cs_list = []               # Tracks thread names in CS
cs_lock = threading.Lock() # Protect cs_list and current_cs_count
current_cs_count = 0       # Tracks how many threads are currently in CS

def try_enter(thread_name):
    global current_cs_count
    acquired = count_sem.acquire(blocking=False)
    if acquired:
        with cs_lock:
            cs_list.append(thread_name)
            current_cs_count += 1
            print(f"[{thread_name}] ENTER CS → current count: {current_cs_count}, threads: {cs_list}", flush=True)
        return True
    else:
        with cs_lock:
            print(f"[{thread_name}] CANNOT ENTER CS → currently in CS: {cs_list}, count: {current_cs_count}", flush=True)
        return False

def leave_cs(thread_name):
    global current_cs_count
    with cs_lock:
        cs_list.remove(thread_name)
        current_cs_count -= 1
        print(f"[{thread_name}] EXIT CS → current count: {current_cs_count}, threads now: {cs_list}", flush=True)
    count_sem.release()

def worker(id):
    thread_name = f"Worker-{id}"
    time.sleep(random.uniform(0, 2))
    print(f"[{thread_name}] REQUESTS CS", flush=True)
    while not try_enter(thread_name):
        time.sleep(1)
    time.sleep(random.uniform(1, 2))
    leave_cs(thread_name)

def short_task(id):
    thread_name = f"Short-{id}"
    time.sleep(random.uniform(0, 2))
    print(f"[{thread_name}] REQUESTS CS", flush=True)
    while not try_enter(thread_name):
        time.sleep(1)
    time.sleep(0.5)
    leave_cs(thread_name)

def long_task():
    thread_name = "Long"
    time.sleep(1)
    print(f"[{thread_name}] REQUESTS CS", flush=True)
    while not try_enter(thread_name):
        time.sleep(1)
    time.sleep(5)
    leave_cs(thread_name)

if __name__ == "__main__":
    # 6 workers
    workers = [threading.Thread(target=worker, args=(i,)) for i in range(1, 7)]
    # 3 short tasks
    shorts = [threading.Thread(target=short_task, args=(i,)) for i in range(1, 4)]
    # 1 long task
    long_thread = threading.Thread(target=long_task)

    # Start threads
    for w in workers: w.start()
    long_thread.start()
    for s in shorts: s.start()

    # Join threads
    for w in workers: w.join()
    long_thread.join()
    for s in shorts: s.join()

    print("\n========== FINAL CS STATE ===========", flush=True)
    print(f"Threads still in CS: {cs_list}", flush=True)
    print(f"Final semaphore counter should be 3 → current_cs_count: {current_cs_count}", flush=True)
