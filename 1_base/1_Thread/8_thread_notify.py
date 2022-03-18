#import multiprocessing
import os, sys
import threading as th
import queue, time, random
# 所谓条件变量，即这种机制是在满足了特定的条件后，线程才可以访问相关的数据。
# 有: Condition 類實現
# acquire(), release(), wait(), notify(), notifyall() 等方法

# 商品類
class Goods():
	def __init__(self):
		self.count = 0

	def add(self, num=1):
		self.count += num

	def sub(self, num=1):
		self.count -= num

	def empty(self):
		return self.count <= 0

# 使用生產者 - 消費者模式
# 生產這 類
class Producer(th.Thread):
	def __init__(self, condition, goods, sleeptime=1):
		th.Thread.__init__(self)
		self.cond = condition	# 通知（條件）
		self.goods = goods		# 商品
		self.sleeptime = sleeptime

	def run(self):
		# 這裏爲什麼要吧數據拷貝出來呢 ？？？
		cond = self.cond	# 拷貝數據
		goods = self.goods
		while True:
			# cond 不是共享的資源，爲什麼要鎖住呢？？？？
			# 應該是： self.cond.acquire()
			############################################
			cond.acquire()	# 鎖住資源
			goods.add()		# self.goods.add() 不應該是這樣嗎
			print("產品數量:", goods.count, "生產者線程")
			cond.notifyAll()		# 喚醒所有等待的線程（消費者線程）
			############################################
			time.sleep(self.sleeptime)

# 消費者 類
class Consumer(th.Thread):
	def __init__(self, condition, goods, sleeptime=2):	# 
		th.Thread.__init__(self)	# call parent's constructor
		self.cond = condition
		self.goods = goods
		self.sleeptime = sleeptime

	def run(self):
		# 爲什麼要拷貝出來呢
		cond = self.cond
		goods = self.goods
		while True:
			time.sleep(self.sleeptime)
			cond.acquire()		# 鎖住資源
			# 等待產品的產生，沒有就等待
			while goods.empty():
				cond.wait()			# 線程阻塞在這裏
			# 有產品出現， 這裏是要執行的操作
			############################################
			goods.sub()
			print("產品數量:", goods.count, "消費者線程")
			############################################
			cond.release()		# 釋放資源

good = Goods()
# 創建一個通知，用於在消費者 和 通知這之間 流通
condition = th.Condition()	# 通知

# 創建生產者對象
pro = Producer(condition, good)
pro.start()

# 創建消費者對象
con = Consumer(condition, good)
con.start()

if __name__ == '__main__':
	pass












	
