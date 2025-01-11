import threading
from threading import Event, Thread
from datetime import datetime

# Event 是一个缩略版的 Condition
# Event没有锁，无法使线程进入同步阻塞状态。着什么意思？？？
event = Event() # 可以用于压力测试

def my_task():
    event.wait()
    print( f'{datetime.now()} -- {threading.current_thread().name} is running')

for ix in range(10):
    threading.Thread(target=my_task).start()


print('setting all threads...')
event.set() # 通知所有 wait() 的线程



