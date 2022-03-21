import threading as th
import time
from queue import Queue

# 线程同步
# (4) sempahore 可以用来控制开启的线程数目
# 可以参考:Queue put() 等的内部实现，-> 掌握 Semaphore
# 借助 Condition 实现
# freeRTOS 互斥信号量(锁)， 计数信号量(控制线程开启的数目), 二值信号量;
# 各种语言本质操作其实都是一样的，只是各自语法不同, 适用场景不同
# 使用场景:
# (1)爬虫, 当同一个 IP 过于频繁的访问一个 URL 的时候是会被反爬的, 因此就需要限制并发的线程的数量
# 内部实现:
# condition

class HtmlSpider(th.Thread):
    def __init__(self, sem):
        super().__init__(name="spider", daemon=True)    # 设置为守护线程
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("爬取到了一个页面...")
        sem.release()       # release() 会将 semaphore 内部的值 +1

class UrlProducer(th.Thread):
    """生产者，消费者模式"""
    def __init__(self, sem):
        super(UrlProducer, self).__init__(name="t", daemon=True)    # 守护线程
        self.sem = sem

    def run(self):
        for ix in range(20):
            self.sem.acquire()  # 每执行一次 acquire(), 会将 semaphore 内部的值-1， 当值为 0 的时候阻塞到这里
            h = HtmlSpider(self.sem)
            h.start()

# 信号量, 锁 以及 条件等都可以通过参数传递引用(指针)进入
sem = th.Semaphore(1)
th1 = UrlProducer(sem)
th1.setDaemon(True)
th1.start()
th1.join()  # 直接关闭, 主线程结束了, 但是子线程没有结束, 就会出现僵尸线程(zombie)

print("main thread end.")

if __name__ == '__main__':
    pass