import os
import threading as th
import sys
import time

# 計數型信號量 th.Semaphore
# s.acquire(), s.release()

class Num:
	def __init__(self):
		self.num = 0
		self.sem = th.Semaphore(value = 3)	# 計數的最大值是3，因此，最多同時支持三個線程訪問資源
	
	def add(self):
		self.sem.acquire()	# 內部計數值 -1， 被一個線程訪問
		self.num += 1
		num = self.num
		self.sem.release()	# 內部計數值 +1， 被一個線程釋放
		return num

n = Num()	# 全局變量

# 線程
class jdThread(th.Thread):
	def __init__(self, item):
		th.Thread.__init__(self)	# 調用弗雷的構造函數
		self.item = item
#run(self)
#    Method representing the thread's activity.
#    
#    You may override this method in a subclass. The standard run() method
#    invokes the callable object passed to the object's constructor as the
#    target argument, if any, with sequential and keyword arguments taken
#    from the args and kwargs arguments, respectively.
# run 是實現父類的一個方法
	def run(self):
		time.sleep(2)
		value = n.add()
		print(self.item, value)

# 創建 100 個線程，只能同時允許三個線程訪問 self.num
for item in range(100):
	t = jdThread(item)
	t.start()
	t.join()













if __name__ == '__main__':
	pass
