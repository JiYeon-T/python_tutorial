import ctypes
from threading import Thread
import threading
import inspect
import time


class BlockingTestThread(Thread):
    """Blocking Test Thread
    线程阻塞方法"""
    def __init__(self):
        self._running_flag = False
        self.stop = threading.Event()
        Thread.__init__(self, target=self.test_entery)
    def test_entery(self):
        try:
            # 同步 + 阻塞的方式结束线程(Right Now)
            # 一直阻塞到 sleep 超时后,线程才可以退出
            while not self.stop.wait(1):
                self._running_flag = True
                print('child Start wait')
                # self.stop.wait(100)
                time.sleep(100)
                print('child Done waiting')
        finally:
            self._running_flag = False

    def terminate(self):
        self.stop.set()

if __name__ == "__main__":
    thread = BlockingTestThread()
    thread.start()
    time.sleep(2)
    print('Time sleep 2')
    thread.terminate()
    print("Joining thread")
    thread.join()
    print("Done Joining thread")