---
**为什么要多阅读开源项目？**

**因为学习了很多知识点其实并不知道具体怎么用，又没有实际项目去学习，就只能去找好的开源项目，就这么简单。这个很重要**

---

## Python高并发的重要性

##### 1. 应用场景

web，爬虫，大数据平台，量化交易，AI.....





##### 2.线程同步基础知识

https://www.cnblogs.com/huxi/archive/2010/06/26/1765808.html

```python
import threading
# threading模块提供的方法
threading.currentThread() # 返回当前的线程变量。
threading.enumerate()# 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
threading.activeCount() # 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
# threading 模块提供的类
Thread, Lock, Rlock, Condition, Semaphore, Event, TImer, local
```

- Thread 类的方法

```python
isAlive()
get/setName()
get/setDaemon()
join() # 阻塞当前上下文环境的线程，直到调用此方法的线程终止或到达指定的timeout（可选参数）才继续运行主线程的的后续代码
```

- Lock() 都是用于共享资源的访问
- RLock
- Condition

Condition 内部两层锁

acquire() 和 release() 可以操控这个相关联的锁。其他的方法都必须在这个锁被锁上的情况下使用。wait() 会释放这个锁，阻塞本线程直到其他线程通过 notify() 或 notify_all() 来唤醒它。一旦被唤醒，这个锁又被 wait() 锁上。

使用场景：线程同步使用，两个线程交替运行

- Semaphore

Semaphore（信号量）是计算机科学史上最古老的同步指令之一。Semaphore管理一个内置的计数器，每当调用acquire()时-1，调用release() 时+1。计数器不能小于0；当计数器为0时，acquire()将阻塞线程至同步锁定状态，直到其他线程调用release()。

基于这个特点，Semaphore经常用来同步一些有“访客上限”的对象，比如连接池。

应用场景：

（1）可以用于控制同时开启的线程的数量，控制线程开启上限；

- Event


Event（事件）是最简单的线程通信机制之一：

一个线程通知事件，其他线程等待事件。Event内置了一个初始为False的标志，当调用set()时设为True，调用clear()时重置为 False。wait()将阻塞线程至等待阻塞状态。Event其实就是一个简化版的 Condition。

**Event没有锁，无法使线程进入同步阻塞状态。**这句话什么意思？？？



---

**熟练掌握Thread、Lock、Condition就可以应对绝大多数需要使用线程的场合，某些情况下local也是非常有用的东西。本文的最后使用这几个类展示线程基础中提到的场景：**

---



