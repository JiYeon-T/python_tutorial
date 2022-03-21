import threading as th
import time

barrier = th.Barrier(3) # 要等待被等待三次, 线程才可以继续执行

def init_db():
    print('init db')
    time.sleep(2)
    print('db init')
    barrier.wait()
    print("db running......")

def init_cache():
    print('init cache')
    time.sleep(1)
    print('init cache')
    barrier.wait()
    print("cache running......")

th.Thread(target=init_db, name="db").start()
th.Thread(target=init_cache, name="cache").start()

print("\r\n\r\ninit is complete")
barrier.wait()
print('\r\n\r\nall thread keep runinng ')
