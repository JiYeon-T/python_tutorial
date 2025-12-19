
 
import threading
import queue,time,random

# 一个简单的生产消费者模型，通过条件变量的控制产品数量的增减，调用一次生产者产品就是+1，调用一次消费者产品就会-1.



# 使用 Condition 类来完成，由于它也可以像锁机制那样用，所以它也有 acquire 方法和 release 方法，而且它还有
# wait， notify， notifyAll 方法。


class Goods(object):
    """产品类"""
    def __init__(self):
        self.count = 0

    def __add__(self, num = 1):
        """定义魔法方法, 重载运算符 +
        :return 这个魔法方法必须要返回自己, self"""
        self.count += num
        return self

    def __sub__(self, num = 0):
        """定义魔法方法, 重载运算符 -
        :return 这个魔法方法必须要返回自己, self"""
        if self.count>=0:
            self.count -= num
        return self

    def empty(self):
        return self.count <= 0
 
class Producer(threading.Thread):
    """生产者类"""
    def __init__(self, condition, goods, sleeptime = 1):#sleeptime=1
        threading.Thread.__init__(self)
        self.cond = condition
        self.goods = goods
        self.sleeptime = sleeptime

    def run(self):
        cond = self.cond
        goods = self.goods
        while True:
            cond.acquire()#锁住资源
            goods = goods + 1
            print("产品数量:", goods.count, "生产者线程")
            cond.notifyAll() #唤醒所有等待的线程--》其实就是唤醒消费者进程
            cond.release() #解锁资源
            time.sleep(self.sleeptime)
 
class Consumer(threading.Thread):#消费者类
    def __init__(self, condition, goods, sleeptime = 2):#sleeptime=2
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
            goods -= 1
            print("产品数量:",goods.count,"消费者线程")
            cond.release()#解锁资源

g = Goods()
c = threading.Condition()

if __name__ == '__main__':
    pro = Producer(c, g)
    pro.start()

    con = Consumer(c, g, sleeptime=0.5)
    con.start()

    # print(type(g))
    # if isinstance(g, Goods):
    #     print("True")
    # else:
    #     print("False")
    # print(type(g), repr(g.count))