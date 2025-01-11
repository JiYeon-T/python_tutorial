import os
import threading as th
import sys
import time


class Num():
	"""Lock test"""
	def __init__(self, num):
		self.num = num
		self.lock = th.Lock() # Lock, 注意 L 大寫

	def add(self):
		"""修改共享資源的方法"""
		self.lock.acquire()
		self.num += 1
		self.lock.release()
		print('num = %d' % self.num)

	def sub(self):
		"""修改共享資源的方法"""
		self.lock.acquire()
		self.num -= 1
		self.lock.release()
		print('num = %d' % self.num)

	def print_num(self):
		"""不修改共享資源的方法,不用枷鎖"""
		print('num = %d' % self.num)

N = Num(100)

def process_num(index):
	"""线程入口函數"""
	global N # 使用全局變量
	print('Tthread index = %d ' % index)
	time.sleep(1)
	N.print_num()

if __name__ == '__main__':
	for i in range(10):
		sub_thread = th.Thread(target=process_num, args=(i, ))
		# sub_thread.setDaemon(True) # 设置为守护线程, 主线程结束, 子线程结束
		sub_thread.start()

	
