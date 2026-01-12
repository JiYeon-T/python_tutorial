import threading
import threading as th
import time
import logging


def __timer_test():
    """
    Timer 是 Thread 的派生类
    默认情况下是只执行一次的(onshot)
    通过 oneshot 的 Timer 实现 periodic 的 timer
    """
    count = 1
    def timer_callback(interval):
        global count
        print(count)
        count += 1
        timer = threading.Timer(interval=2, function=timer_callback, args=(interval, ))
        timer.start()

    interval = 2
    tim = th.Timer(interval=interval, function=timer_callback, args=(interval, ))
    tim.start()

if __name__ == '__main__':
    __timer_test()