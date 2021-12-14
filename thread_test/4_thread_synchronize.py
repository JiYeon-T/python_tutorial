import threading as th
import time
#from queue import  Queue
#线程同步
# (1)Lock, 控制对于共享变量的使用，效率会比较低, 还存在死锁问题(两种情况)
# (2)RLock(可重入的锁)
# (3)Condition
num = 1
lock = th.Lock()    #
lock2 = th.RLock()  # 可重入锁, 可以多次 acquire()， 普通的锁多次 acquire() 会死锁
# 锁
def add():
    global num
    global lock
    for ix in range(1000000):
        lock.acquire()
        num += 1
        lock.release()

def sub():
    global num
    global lock
    for ix in range(1000000):
        lock.acquire()
        num -= 1
        lock.release()

print("before:num = {}".format(num))
th1 = th.Thread(target=add, name="thread1")
th2 = th.Thread(target=sub, name="thread2")
th1.start()
th2.start()
th1.join()
th2.join()
print("after:num = {}".format(num))

# Condition



if __name__ == '__main__':
    pass