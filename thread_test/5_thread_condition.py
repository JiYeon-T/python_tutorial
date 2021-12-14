import threading as th
import time
from threading import Condition

#from queue import  Queue
th.Condition    # Condition 类实现了 __enter__, __exit__ 就可以使用魔法方法 with 打开
# (3)condition
#Condition 具有通知的功能, cond.wait() 等待某一个通知; notify() 通知某一个线程
#线程同步, 让两个线程轮番执行(依次执行)
# 实现原理: 内部有两层锁
num = 1

class XiaoAi(th.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:     # 可以使用 with 或者 acquire()/release()
            print("我斯小艾")       # step1
            self.cond.notify()  # 通知 其他线程
            self.cond.wait()    # 等待通知, step3
            # time.sleep(5)
            print("今天天气怎么养鸭？")
            self.cond.notify()

class TianMaoJingLing(th.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        self.cond.acquire()
        self.cond.wait()    # 等待通知 , step2
        print("你好, 俺是天猫")
        self.cond.notify()  # 通知其他线程
        # time.sleep(5)
        self.cond.wait()    # step4
        print("天气还可以")
        self.cond.release()

# 两个线程的启动顺序很重要
cond = th.Condition()
tianmao = TianMaoJingLing(cond)
xiaoai = XiaoAi(cond)
tianmao.start()
xiaoai.start()

# 主线程阻塞等待子线程结束
tianmao.join()
xiaoai.join()

# 子线程都结束 -> 主线程结束
print("main thread end.")

if __name__ == '__main__':
    pass
