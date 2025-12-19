import sys
import threading
import time
# python 中的线程同步方式:Lock, RLock(), Condition, Semaphore, BoundedSemaphore, Event, Barier
# 递归锁:RLock, 同一个线程可以多次获取同一个锁, 而不会导致死锁,
# 对于某些特殊场景可以使用, 内部会维护一个计数器, 只有计数器的值变为零其他线程才可以获取这个锁
lock = threading.Lock()
rlock = threading.RLock()

# Lock:
# def thread_fun(arg):
#     while True:
#         lock.acquire(blocking=True, timeout=5)
#         try:
#             # 访问共享数据
#             # lock.acquire(blocking=True, timeout=5) #dead lock
#             print(f"thread running:{arg}")
#             time.sleep(1)
#         finally:
#             lock.release()

# RLock:
def thread_fun(arg):
    while True:
        rlock.acquire(blocking=True)
        try:
            # 访问共享数据
            rlock.acquire(blocking=True)
            print(f"thread running:{arg}")
            time.sleep(1)
            rlock.release()
        finally:
            rlock.release()

def lock_test():
    th1 = threading.Thread(target=thread_fun, name="thread1", args=(1, ))
    th2 = threading.Thread(target=thread_fun, name="thread2", args=(2, ))
    th1.start()
    th2.start()
    th1.join()
    th2.join()

class Worker(threading.Thread):
    cnt = 0
    def run(self):
        Worker.cnt += 1
        print(f"Running {Worker.cnt}")
        sys.exit(0)

    @classmethod
    def entry(cls):
        Worker.cnt += 1
        print(f"Running {Worker.cnt}")

if __name__ == '__main__':
    # lock_test()
    w = Worker()
    w.start() # ERROR
    # th = threading.Thread(target=Worker.entry)
    # th.setDaemon(True)
    # th.start()

    time.sleep(1)
    w.start()
    # th = threading.Thread(target=Worker.entry)
    # th.setDaemon(True)
    # th.start()

    time.sleep(1)
    w.start()
    # th = threading.Thread(target=Worker.entry)
    # th.setDaemon(True)
    # th.start()

    time.sleep(3)
