import threading as th
import os
import sys
import time


# 线程同步:
# 多个进程可以协同工作来完成一项任务，通常需要共享数据。
# 所以在多进程之间保持数据的一致性就很重要，需要共享数据协同的进程必须以适当的策略来读写数据。
# 同步原语和线程的库类似。

# Q:还是不行????，明明是 th.Lock() 不知道問題出在哪兒
# A: 2s 后主线程退出了, 但是子线程还并没有结束, 因此每次打印的值不同
# 临界资源即那些一次只能被一个线程访问的资源，
# eg:典型例子就是打印机，它一次只能被一个程序用来执行打印功能，
# 因为不能多个线程同时操作，而访问这部分资源的代码通常称之为临界区。


# 1. Lock
class Num(object):
	def __init__(self):
		self.num = 0
		self.lock = th.Lock()  # 創建一個鎖，對象

	def add(self):
		self.lock.acquire()  # 加鎖
		for i in range(1000000):
			self.num += 1
		num = self.num  # 拷貝出來數據，再返回,相當於拷貝;直接返回的話傳遞的是引用
		self.lock.release()  # 釋放鎖
		return num

	def __repr__(self):
		return str(self.num)


test_num = Num()  # 全局變量 n,是共享資源


def thread_lock_test1():
	"""通过锁实现线程同步"""

	class AdderThread(th.Thread):
		"""
		创建现成的另一种方式
		創建一了類，繼承自 th.Thread()"""

		def __init__(self, item):
			th.Thread.__init__(self)  # 調用父類的構造函數
			self.item = item

		def run(self):
			# time.sleep(2)  # 模拟线程操作耗时
			test_num.add()  # 將 num+1,
			return

	print(f"before:{repr(test_num)}")
	for i in range(100):
		child_thread = AdderThread(i)  # 创建子线程
		child_thread.start()
		# print(repr(test_num))
		# child_thread.join() # 主线程阻塞等待子线程结束, 这里使得子线程一個接一個的運行

	print("main start sleep")
	# TODO: 子线程同时开始, 主线程如何等待所有子线程结束后再继续运行??? barrier??
	# 即主线程阻塞等待多个子线程结束
	# 这里需要由简单的 sleep 改为等所有子线程结束擦可以测试
	time.sleep(2)  # 阻塞等待所有子线程结束
	print("after:", repr(test_num))


if __name__ == '__main__':
	thread_lock_test1()
