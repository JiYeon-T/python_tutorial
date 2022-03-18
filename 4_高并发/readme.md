---

**为什么要多阅读开源项目？**

**因为学习了很多知识点其实并不知道具体怎么用，又没有实际项目去学习，就只能去找好的开源项目，就这么简单。这个很重要**

---

## Python高并发的重要性

##### 1. 应用场景

web，爬虫，大数据平台，量化交易，AI.....





##### 2.基础知识

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

内部两层锁

- Semaphore

可以用于控制同时开启的线程的数量

- Event





