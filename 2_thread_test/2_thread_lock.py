import threading as th

# lock 等信号使用的两种方式
# 通常选择 RLock()
# 方法1: 复杂
# lock.acquire()
# try:
#     pass
# finally:
#     lock.release()
# 方法2:实现了 __enter__() 和 __exit__() 就可以使用 with
# with lock:
#     pass
import time


class Account():
    def __init__(self, balance):
        self.balance = balance
        self.lock = th.Lock()

    def increase(self, amount):
        self.balance += amount


account = Account(0)

def transfer():
    global account
    # account.lock.acquire()
    with account.lock: # 粒度,
        for ix in range(2000000):
            account.increase(1)
    # account.lock.release()


# th1 = th.Thread(target=transfer)
# th2 = th.Thread(target=transfer)
# th1.start()
# th2.start()
# th1.join()
# th2.join()
#
# print(account.balance)
##########################################################################
# RLock() 可重入锁
# 用于保护同一个过程中不同的资源????
rlock = th.RLock()
def fun():
    print(th.current_thread().getName(), "开始")
    rlock.acquire()
    for i in range(5):
        print(th.current_thread().getName(), f"running...{i}")
        #time.sleep(1)
        rlock.acquire()
        for j in range(2):
            print(th.current_thread().getName(), f"running...{i}-{j}")
            time.sleep(1)
        rlock.release()
    rlock.release()
    print(th.current_thread().getName(), "结束")

if __name__ == '__main__':
    th1 = th.Thread(target=fun, name="thread1")
    th2 = th.Thread(target=fun, name="thread2")
    th1.start()
    th2.start()
    print("主线程结束")


