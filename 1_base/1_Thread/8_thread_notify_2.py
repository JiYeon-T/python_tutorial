"""
一个简单的生产消费者模型，通过条件变量的控制产品数量的增减，调用一次生产者产品就是+1，调用一次消费者产品就会-1.
"""
 
"""
使用 Condition 类来完成，由于它也可以像锁机制那样用，所以它也有 acquire 方法和 release 方法，
而且它还有wait， notify， notifyAll 方法 —— 可以用于线程同步。
"""
 
import threading
import queue,time,random
 
class Goods:#产品类
    def __init__(self):
        self.count = 0
    def add(self,num = 1):
        self.count += num
    def sub(self):
        if self.count>=0:
            self.count -= 1
    def empty(self):
        return self.count <= 0
 
class Producer(threading.Thread):#生产者类
    def __init__(self,condition,goods,sleeptime = 1):#sleeptime=1
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime
    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            cond.acquire()#锁住资源
            goods.add()
            print("产品数量:",goods.count,"生产者线程")
            cond.notifyAll()#唤醒所有等待的线程--》其实就是唤醒消费者进程
            cond.release()#解锁资源
            time.sleep(self.sleeptime)
 
class Consumer(threading.Thread):#消费者类
    def __init__(self,condition,goods,sleeptime = 2):#sleeptime=2
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime
    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            time.sleep(self.sleeptime)
            cond.acquire()#锁住资源
            while goods.empty():#如无产品则让线程等待
                cond.wait()
            goods.sub()
            print("产品数量:",goods.count,"消费者线程")
            cond.release()#解锁资源
 
g = Goods()
c = threading.Condition()
 
pro = Producer(c,g)
pro.start()
 
con = Consumer(c,g)
con.start()
