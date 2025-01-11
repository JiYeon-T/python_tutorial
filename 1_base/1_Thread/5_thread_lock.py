import threading as th
import os
import sys
import time
# 變異不過，明明是 th.Lock() 不知道問題出在哪兒

# 临界资源即那些一次只能被一个线程访问的资源，
# eg:典型例子就是打印机，它一次只能被一个程序用来执行打印功能，因为不能多个线程同时操作，而访问这部分资源的代码通常称之为临界区。
# 1. Lock

class Num(object):
	def __init__(self):
		self.num = 0
		self.lock = th.Lock() # 創建一個鎖，對象

	def add(self):
		self.lock.acquire() # 加鎖
		self.num += 1
		num = self.num # 拷貝出來數據，再返回,相當於拷貝;直接返回的話傳遞的是引用
		self.lock.release() # 釋放鎖
		return num

	def __repr__(self):
		return str(self.num)

g_n = Num() # 全局變量 n,是共享資源


class jbThread(th.Thread):
	"""創建一了類，繼承 th.Thread()"""
	def __init__(self, item):
		th.Thread.__init__(self) # 調用父類的構造函數
		self.item = item		

	def run(self):
		time.sleep(2)
		value = g_n.add() # 將 num+1,
		return (self.item, value)

if __name__ == '__main__':
	for item in range(5):
		t = jbThread(item)
		t.start()
		print(repr(g_n))
		# t.join() # 主线程阻塞等待子线程结束, 这里使子线程一個接一個的運行
	time.sleep(2.0) # 阻塞等待所有子线程结束
	print("final:", repr(g_n))


