import os
import threading as th
import sys

class Num():
	"""Lock test"""
	def __init__(self, num):
		self.num = num
		self.lock = th.Lock()	# lock

	def add(self):
		"""修改共享資源的方法"""
		self.lock.acquire()
		self.num += 1
		print('num = %d' % self.num)
		self.lock.release()

	def sub(self):
		"""修改共享資源的方法"""
		self.lock.acquire()
		self.num -= 1
		print('num = %d' % self.num)
		self.lock.release()

	def print_num(self):
		"""不修改共享資源的方法,不用枷鎖"""
		print('num = %d' % self.num)

N = Num(100)

def process_num(index):
	"""線程入口函數"""
	global N	# 使用全局變量
	#N.print_num()
	#N.add()
	N.sub()
	print('Tthread index = %d ' % index)

if __name__ == '__main__':
	for ix in range(10):
		# args 作爲線程參數必須是可迭代類型，元組
		sub_thread = th.Thread(target=process_num, args=(ix,))
		# sub_thread.setDaemon(True)
		sub_thread.start()

	
