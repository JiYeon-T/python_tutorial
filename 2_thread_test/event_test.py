import threading
import time

# 可以通过 event 来判断线程当前的运行状态, Event().is_set()

# event = threading.Event()

events = []
for ix in range(10):
    events.append(threading.Event())

def thread_fun(arg):
    global events
    while True:
        idx = arg
        events[idx].wait() # 等待事件
        print(f"thread:{arg} running")
        events[idx].clear() # 清除事件标志位,不清楚就一直为 True

def event_test():
    global event
    for idx in range(10):
        th = threading.Thread(target=thread_fun, name=f"thread-{idx}", args=(idx, ))
        th.start()
    time.sleep(1)
    for idx in range(10):
        events[idx].set() # 发送事件
        time.sleep(1)
    time.sleep(1000)

def os_test():
    import os
    path = "abc/test.txt"
    print(os.path.dirname(path))
    print(os.path.abspath(__file__))

if __name__ == '__main__':
    # event_test()
    os_test()