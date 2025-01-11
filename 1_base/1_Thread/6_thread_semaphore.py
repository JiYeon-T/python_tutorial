import os
import threading as th
import sys
import time

# 計數型信號量 th.Semaphore
# s.acquire(), s.release()

class Num:
	def __init__(self):
		self.num = 0
		self.sem = th.Semaphore(value = 3) # 計數的最大值是3，因此，最多同時支持三個線程訪問資源
	
	def add(self):
		self.sem.acquire() # 內部計數值 -1， 被一個線程訪問
		self.num += 1
		num = self.num
		self.sem.release() # 內部計數值 +1， 被一個線程釋放
		return num

n = Num() # 全局變量

# 線程
class jdThread(th.Thread):
	"""多线程的另一种实现方式, 继承 Thread 类
		重载 run 方法"""
	def __init__(self, item):
		th.Thread.__init__(self) # 調用弗雷的構造函數
		self.item = item
	# run 是實現父類的一個方法
	def run(self):
		time.sleep(2)
		value = n.add()
		print(self.item, value)


if __name__ == '__main__':
	for item in range(100):
		t = jdThread(item) # 創建 100 個線程，只能同時允許三個線程訪問 self.num
		t.start()
		t.join()













if __name__ == '__main__':
	pass
