import threading
import time

product = 500
con = threading.Condition(lock=threading.Lock())

# 疑问: 每一个线程等条件之前都必须先获取锁, 那为什么还需要 notifyAll 接口呢
# 只有一个线程可以等条件吧???

class Producer(threading.Thread):
    """产品不够 500 就补充 50 个"""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        global product
        global con
        while True:
            if con.acquire(): # 持锁
                if product >= 500:
                    con.wait() # 等待
                else:
                    product += 50
                    print(f"{self.name} produce 50 products num:{product}")
                    con.notify() # 处理完成,通知消费者
                con.release() # 释放锁
                time.sleep(1)


class Consumer(threading.Thread):
    def __init__(self, name):
        """product 多于 100 个就消耗 10 个"""
        super().__init__()
        self.name = name

    def run(self):
        global product
        global con
        while True:
            if con.acquire(): # 持锁
                if product <= 100:
                    con.wait() # 等待
                else:
                    product -= 10
                    print(f"{self.name} consume 10 products num:{product}")
                    con.notify() # 通知
                con.release()
                time.sleep(1)


def cond_test():
    # 2 producer
    for idx in range(2):
        p = Producer(f"producer-{idx}")
        p.start()

    # 3 consumer
    for idx in range(3):
        c = Consumer(f"consumer-{idx}")
        c.start()

if __name__ == '__main__':
    cond_test()
    time.sleep(1000)