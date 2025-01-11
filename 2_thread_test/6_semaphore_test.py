import threading as th
import time
from datetime import datetime

class Service():
    def __init__(self):
        # 创建信号量, 控制开启线程的数目
        self.sema = th.BoundedSemaphore(value=3)   #

    def serv(self):
        with self.sema:
            print(f'{datetime.now()} -- saving {th.current_thread().getName()}')
            #print("creat thread.")
            time.sleep(1)

# 创建线程
service = Service()
for ix in range(10):
    th.Thread(target=lambda service : service.serv(), args=(service, )).start()
