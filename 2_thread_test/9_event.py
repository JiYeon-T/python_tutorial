import threading
from threading import Event, Thread
from datetime import datetime

event = Event() # 可以用于压力测试

def my_task():
    event.wait()
    print( f'{datetime.now()} -- {threading.current_thread().name} is running')

for ix in range(10):
    threading.Thread(target=my_task).start()


print('setting all threads...')
event.set() # 通知所有 wait() 的线程



