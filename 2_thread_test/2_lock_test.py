import threading as th
import time


class Client(th.Thread):
    g_balance = 1000
    g_balance_lock = th.Lock()
    def __init__(self):
        super().__init__()
        pass

    def __del__(self):
        pass

    def run(self):
        while True:
            self.g_balance_lock.acquire()
            self.g_balance += 1
            print(f"{th.current_thread().ident}:{self.g_balance}")
            self.g_balance_lock.release()
            time.sleep(2)


if __name__ == '__main__':
    a = Client()
    # a.setDaemon(True)
    b = Client()
    # b.setDaemon(True)
    a.start()
    b.start()
    a.join()
    b.join()