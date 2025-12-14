#import multiprocessing
import os, sys
import threading as th
import time, random
import queue		# 消息隊列
# task_done(), put(), 
# queue有一个未完成任务数量num，put依次num+1，task依次num-1.任务都完成时任务结束。

'''
1.创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
2.将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
3.每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
4.在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
5.对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。
'''

class jdThread(th.Thread):
	def __init__(self, index, queue):
		th.Thread.__init__(self)
		self.index = index
		self.queue = queue	# 創建一個隊列

	def run(self):
		while True:
			time.sleep(1)
			# queue.get() 函數會阻塞
			item = self.queue.get()	# 出隊, item 就是隊列中的數據
			if item is None:
				break
			print("序號:", self.index, "任務", item, "完成")
			self.queue.task_done()	# task_done 方法是未完成的任務數量 -1

'''
初始化函数接受一个数字来作为该队列的容量，如果传递的是
一个小于等于0的数，那么默认会认为该队列的容量是无限的.
'''
q = queue.Queue(0)

for i in range(2):
	thread_i = jdThread(i, q)	# 2個線程同時處理隊列中的消息
	thread_i.start()
	

for i in range(10):		# 模擬向隊列中賽數據
	q.put(i)
	time.sleep(2)
	


if __name__ == '__main__':
	pass



