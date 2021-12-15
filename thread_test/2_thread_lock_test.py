import threading as th

# lock 等信号使用的两种方式
# 通常选择 RLock()
# 方法1: 复杂
# lock.lock()
# try:
#     pass
# finally:
#     lock.release()
# 方法2:
# with lock:
#     pass

class Account():
    def __init__(self, balance):
        self.balance = balance
        self.lock = th.Lock()

    def increase(self, amount):
        self.balance += amount


account = Account(0)

def transfer():
    global account
    with account.lock: # 粒度
        for ix in range(2000000):
            account.increase(1)
    # do something

th1 = th.Thread(target=transfer)
th2 = th.Thread(target=transfer)
th1.start()
th2.start()
th1.join()
th2.join()

print(account.balance)