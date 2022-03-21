import threading
import logging
import time

# 对所有线程同步以及通信的方法进行简单练习
DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"
LOG_FORMAT = "%(asctime)s %(threadName)s|%(thread)d : %(message)s"
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt=DATE_FORMAT)
alist = None
cond = threading.Condition()

def doSet():
    """ trhea entry function """
    global alist
    logging.debug("thread start")
    if cond.acquire():
        logging.debug("got lock1")
        while alist is None:
            cond.wait()
            logging.debug("got lock2")
            logging.debug("set running...")
        for i in range(len(alist))[::-1]:
            alist[i] = 1 # 修改共享数据
        cond.release()
    logging.debug("thread end")

def doPrint():
    """ trhea entry function """
    global alist
    logging.debug("thread start")
    if cond.acquire():
        logging.debug("got lock1")
        while alist is None:
            cond.wait()
            logging.debug("got lock2")
            logging.debug("print running...")
        for i in alist:
            logging.info(i) # 打印共享数据
        cond.release()
    logging.debug("thread end")

def doCreate():
    """ trhea entry function - 生产者"""
    global alist
    logging.debug("thread start")
    if cond.acquire():
        logging.debug("got lock1")
        logging.debug("create running..")
        if alist is None:
            alist = [0 for i in range(10)]
            #cond.notify()
            cond.notifyAll()
        cond.release()
    logging.debug("thread end")

def test():
    logging.debug("main thread started.")
    thread_pool = []

    th2 = threading.Thread(target=doPrint, name="Printer")
    th1 = threading.Thread(target=doSet, name="Setter")
    th3 = threading.Thread(target=doCreate, name="Creater")
    thread_pool.append(th1)
    thread_pool.append(th2)
    thread_pool.append(th3)
    for ix in thread_pool: # 开始
        ix.start()
    for ix in thread_pool: # 主线程阻塞等待
        ix.join()

    logging.debug("main thread end.")

if __name__ == '__main__':
    test()