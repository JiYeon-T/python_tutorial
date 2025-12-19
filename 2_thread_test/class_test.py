import os
import sys
import threading
import time
import re

class Animal():
    # 类变量
    TYPE = "A"
    def __init__(self):
        print("Animal Constructor type:" + self.TYPE)
    def __del__(self):
        print("Animal deconstructor animal type:" + self.TYPE)

class Dog(Animal):
    # TYPE = "D"
    def __init__(self):
        super(Dog, self).__init__()
        print("Dog Constructor type:" + self.TYPE)

    def __del__(self):
        super(Dog, self).__del__()
        print("Dog deconstructor animal type:" + self.TYPE)

def timer_test():
    while True:
        print("running")
        time.sleep(2)

def test():
    timer = threading.Timer(function=timer_test, interval=5)
    timer.setDaemon(True)
    timer.start()


if __name__ == '__main__':
    # a = Animal()
    # d = Dog()

    # test()
    # time.sleep(10000)

    # a = [0, 1, 2, 3, 4]
    # print(f"{a[:]}")
    # print(f"{a[:1]}")
    # print(f"{a[1:2]}")
    # print(f"{a[0:2]}") # 索引, 包含前索引元素, 不包含后索引元素

    str = "open file success:retransmission start length:146330"
    # _get_continue_transfer_position(str)

    print(str)