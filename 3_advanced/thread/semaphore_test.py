import os
import threading as th
import sys
import time

# 計數型信號量: th.Semaphore
# s.acquire(), s.release()


class Num(object):
	def __init__(self):
		self.num = 0
		self.sem = th.Semaphore(value=1)  # 计数型信号量, 計數的初始值是3，因此，最多同時支持三個線程訪問資源
		# for i in range(100):  # 刚初始化就释放 100 次, 导致后续所有线程都立即执行结束
		# 	self.sem.release()
		# print(f"{self.sem._value}") # 101

	def add(self):
		self.sem.acquire()  # 內部計數值 -1， 被一個線程訪問
		self.num += 1
		time.sleep(1)  # 拿信号量一秒钟, 导致线程被挨个执行
		self.sem.release()  # 內部計數值 +1， 被一個線程釋放


n = Num()  # 全局變量


def sem_example1():
	# 線程
	class AdderThread(th.Thread):
		"""多线程的另一种实现方式, 继承 Thread 类
			重载 run 方法"""

		def __init__(self, item):
			th.Thread.__init__(self)  # 調用弗雷的構造函數
			self.item = item

		def run(self):
			"""run 是實現父類的一個方法, 创建线程需要重写该方法"""
			global n
			n.add()
			print(f"thread {self.item} is running, num:{n.num}", end="\n\n")
			time.sleep(1)

	for i in range(100):
		t = AdderThread(i)  # 創建 100 個線程，只能同時允許三個線程訪問 self.num
		t.start()
		# t.join()  # 这里会阻塞的, 直到子线程结束

	time.sleep(20)
	print('main exit')


if __name__ == '__main__':
	sem_example1()
