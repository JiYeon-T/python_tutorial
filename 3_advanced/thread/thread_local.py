import threading
import time
import logging


# get thread-local implementation, either from the thread
# module, or from the python fallback
# try:
#     from _thread import _local as local
# except ImportError:
#     from _threading_local import local

# local是一个小写字母开头的类，用于管理 thread-local（线程局部的）数据。
# 对于同一个local，线程无法访问其他线程设置的属性；线程设置的属性不会被其他线程设置的同名属性替换。
# 属性字典, 通过 key 进行访问
# 应用场景: 这个 local 类有什么用呢??
# TODO:




format = "%(asctime)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=format)
local = threading.local()
local.tname = 'main'

def fun():
    global local
    local.tname = 'notmain'
    logging.debug(threading.current_thread().getName()+'thread running...'+local.tname)

def test():
    th1 = threading.Thread(target=fun, name="fun")
    th1.start()
    logging.debug('main thread running...'+local.tname)


if __name__ == '__main__':
    test()