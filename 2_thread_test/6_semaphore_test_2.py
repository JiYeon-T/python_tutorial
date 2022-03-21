import threading as th
import logging
import time

format = "%(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=format)

def fun(sema):
    """ 线程入口函数 """
    logging.debug(th.current_thread().getName() + " created")
    sema.acquire()
    logging.debug(th.current_thread().getName() + " running...")
    time.sleep(2)
    sema.release()
    logging.debug(th.current_thread().getName() + " end")


def test():
    sema = th.Semaphore(1)
    thread_list = []
    for ix in range(10):
        temp = th.Thread(target=fun, name=f"thread{ix}", args=(sema, ))
        #temp.setDaemon(True)
        thread_list.append(temp)
        temp.start()



if __name__ == '__main__':
    test()