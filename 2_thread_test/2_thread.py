import threading as th
import time

##########################################################################
# 1.threading
# threading基于Java的线程模型设计。
# 锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），
# 而在Python中则是独立的对象。
# Python Thread提供了Java Thread的行为的子集；没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。
# Java Thread中的部分被 Python 实现了的静态方法在 threading 中以模块方法的形式提供。

# 方法1：直接使用 Thread()，适用于线程简单的情况
# 使用：(1)多线程使用线程池的话通常使用这种方法;
# (2) 简单线程;
def get_detail_html():
    print("get_detail_html started.")
    time.sleep(2)
    print("get_detail_html ended.")

def get_detail_list():
    print("get_detail_list started.")
    time.sleep(2)
    print("get_detail_list ended.")

# th1 = th.Thread(target=get_detail_html)
# th2 = th.Thread(target=get_detail_list)
# 设置守护线程，只要主线程结束，子线程不管执行到哪里都义无反顾的结束， 设置要在 start() 前面
# 或者:th1 = th.Thread(target=get_detail_html, Daemon=True)
# th1.setDaemon(True)
# th2.setDaemon(True)
# time_start = time.time()
# th1.start()
# th2.start()
#th1.join()              # 主线程阻塞在这里等待子线程结束，然后主线程才结束
#th2.join()
#print('time used:{} s'.format(time.time() - time_start))

##########################################################################
# 放法2：继承 Thread 实现多线程， 适用于线程复杂的时候
# 用法:  复杂线程时
# 重载 run 放法
class GetDetailHtml(th.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        """重载 父类的 run() 方法"""
        print("get_detail_html started.")
        time.sleep(2)
        print("get_detail_html ended.")


class GetDetailList(th.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get_detail_list started.")
        time.sleep(2)
        print("get_detail_list ended.")

# th1 = GetDetailHtml("html_thread")
# th2 = GetDetailList("list_thread")
# time_start = time.time()
# th1.start()
# th2.start()
# th1.join()
# print("主线程阻塞等待th1结束")
# th2.join()
# print("主线程阻塞等待th2结束")
# print('time used:{} s'.format(time.time() - time_start))

if __name__ == '__main__':
    pass