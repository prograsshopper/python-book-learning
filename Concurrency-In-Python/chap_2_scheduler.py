import threading, time, random

counter = 1

def workerA():
    global counter
    while counter < 1000:
        counter += 1
        print(f'Worker A is incrementing counter to {counter}')
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)

def workerB():
    global counter
    while counter > -1000:
        counter -= 1
        print(f'Worker B is decrementing counter to {counter}')
        sleep_time = random.randint(0, 1)
        time.sleep(sleep_time)

def main():
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    
    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()
    
    t1 = time.time()
    
    print(f"Execution Time: {t1-t0}")


if __name__ == '__main__':
    main()