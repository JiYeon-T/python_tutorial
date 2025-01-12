import threading as th

class Account():
    def __init__(self, balance):
        self.balance = balance

    def increase(self, amount):
        self.balance += amount



account = Account(0)

def transfer():
    global account
    for ix in range(2000000):
        account.increase(1)

th1 = th.Thread(target=transfer) # 多线程共享变量存在竞争问题, 不可以直接使用
th2 = th.Thread(target=transfer)
th1.start()
th2.start()
th1.join()
th2.join()
#th1.exit() # 线程如何显示的让他结束, 还是说必须要 fun() 运行完才可以结束


print(account.balance)