import threading
import time

sema = threading.Semaphore(value=2) # 同事可以有 value 个线程获取到信号量

def thread_fun(arg):
    global sema
    while True:
        sema.acquire()
        print(f"thread:{arg} running")
        time.sleep(2)
        sema.release()
        time.sleep(1)

def sema_test():
    global sema
    for idx in range(10):
        th = threading.Thread(target=thread_fun, name=f"thread-{idx}", args=(idx, ))
        th.start()

if __name__ == '__main__':
    sema_test()