import threading
import threading as th
import time
import logging

# Timer 是 Thread 的派生类
# 默认情况下是只执行一次的
# 通过 oneshot 的 Timer 实现 periodic 的 timer
count = 1
def fun(interval):
    global count
    # for ix in range(10):
    #     print(ix, interval)
    #     time.sleep(1)
    print(count)
    count += 1
    interval = 2
    timer = threading.Timer(interval=2, function=fun, args=(interval, ))
    timer.start()

def test():
    interval = 2
    tim = th.Timer(interval=interval, function=fun, args=(interval, ))
    tim.start()

if __name__ == '__main__':
    test()