import threading as th
import time
##########################################################################
# 1.threading
# threading基于Java的线程模型设计。
# 锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），而在Python中则是独立的对象。
# Python Thread提供了Java Thread的行为的子集；没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。
# Java Thread中的部分被Python实现了的静态方法在 threading 中以模块方法的形式提供。

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

#########################################################################
# 2._thread 模块
# thread提供了低级别的、原始的线程以及一个简单的锁。
# thread还提供了一个ThreadLocal类用于管理线程相关的数据，名为 thread._local，threading中引用了这个类。
# 由于thread提供的线程功能不多，无法在主线程结束后继续运行，不提供条件变量等等原因，一般不使用thread模块，

# _thread对于进程何时退出没有任何控制。当主线程结束时，所有其他线程也都强制结束。不会发出警告或者进行适当的清理。
# 因而python多线程一般使用较为高级的threading模块，它提供了完整的线程控制机制以及信号量机制。
# 但是这些event, condition, semaphore 都具体是怎么控制的呢?
import _thread
import time

def fun():
    """ 线程入口函数 """
    for ix in range(1000):
        print(ix)
        time.sleep(1)
    print("线程结束")
    _thread.exit()  # 结束当前线程


def thread_test():
    # 创建线程
    th1 = _thread.start_new_thread(fun, (), {})  # 传入元组与字典这两个参数
    print(_thread.get_ident()) # 不是线程 ID, 只是一个魔法数字
    _thread.interrupt_main() # 子线程中结束主线程， raise a KeyBoardInterrupt to interrupt main thread
    lock = _thread.allocate_lock()
    print("lock state:", lock.locked())
    count = 0  # 通过锁控制对全局变量的访问
    if lock.acquire():
        count += 1
        lock.release()
    # thread模块提供的线程都将在主线程结束后同时结束

thread_test()

if __name__ == '__main__':
    pass