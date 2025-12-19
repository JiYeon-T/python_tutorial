import ctypes
import threading
from threading import Thread
import inspect
import time

class BlockingTestThread(Thread):
    def __init__(self):
        self._running_flag = False
        Thread.__init__(self, target=self.test_method)
    def test_method(self):
        try:
            while(self.is_alive()):
                self._running_flag = True
                time.sleep(5)
        finally:
            self._running_flag = False

def _async_raise(tid, exctype):
    '''Raises an exception in the threads with id tid
    通过抛出异常的方式结束线程
    这种方式最号不要使用'''
    if not inspect.isclass(exctype):
        raise TypeError("Only types can be raised (not instances)")
    # 仅仅是将线程结束加入"计划",线程实际结束时间还是要解除阻塞之后;
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(ctypes.c_long(tid), ctypes.py_object(exctype))
    time.sleep(0.1)

def daemon_test():
    """子线程设置为 daemon 线程后_主线程退出, 子线程就退出"""
    print("main enter")
    def entry():
        while True:
            print(f"running {threading.get_ident()}")
            time.sleep(1)
    t = threading.Thread(target=entry)
    t.setDaemon(True) # 主线程退出后, 子线程也退出
    t.start()
    # t.join() # 这里主线程阻塞等待子线程结束
    i = 1
    while i < 5:
        i += 1
        time.sleep(1)
    print("main exit")

def event_test():
    """所有阻塞等待 Event 的线程都会收到事件 """
    event = threading.Event()
    print("main enter")
    def entry():
        while True:
            event.wait()
            event.clear()
            print(f"running {threading.get_ident()}")
            time.sleep(5)
    for i in range(5):
        t = threading.Thread(target=entry)
        t.setDaemon(True)  # 主线程退出后, 子线程也退出
        t.start()

    while True:
        print("--- main running")
        event.set()
        time.sleep(10)
    print("main exit")

def sema_test():
    """所有阻塞等待 Event 的线程都会收到事件 """
    sema = threading.Semaphore(value=0)
    print("main enter")
    def entry():
        while True:
            sema.acquire()
            print(f"child running {threading.get_ident()}")
            time.sleep(5)
    for i in range(5):
        t = threading.Thread(target=entry)
        t.setDaemon(True)  # 主线程退出后, 子线程也退出
        t.start()

    while True:
        print("--- main running")
        in_str = input()
        if in_str == 'a':
            sema.release()
        # time.sleep(10)
    print("main exit")

if __name__ == "__main__":
    # thread = BlockingTestThread()
    # thread.start()
    # _async_raise(thread.ident, SystemExit)
    # print ("Joining thread")
    # thread.join()
    # print ("Done Joining thread")

    # daemon_test()
    # event_test()
    sema_test()
