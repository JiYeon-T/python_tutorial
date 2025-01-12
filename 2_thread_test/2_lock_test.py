import threading as th
import time


class Client(th.Thread):
    g_balance = 0 # 类变量
    g_balance_lock = th.Lock()
    def __init__(self):
        super().__init__()
        pass

    def __del__(self):
        pass

    def run(self):
        for i in range(2000000):
            self.g_balance_lock.acquire()
            Client.g_balance += 1
            # print(f"pid:{th.current_thread().ident}:{self.g_balance}")
            self.g_balance_lock.release()
        else:
            print(Client.g_balance)

if __name__ == '__main__':
    a = Client()
    # a.setDaemon(True)
    b = Client()
    # b.setDaemon(True)
    a.start()
    b.start()
    a.join()
    b.join()
    time.sleep(5)
    print(a.g_balance)