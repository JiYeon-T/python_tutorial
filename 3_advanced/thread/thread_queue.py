#import multiprocessing
import os, sys
import threading
import threading as th
import time, random
import queue  # 消息隊列

# task_done(), put(), 
# queue有一个未完成任务数量num，put依次num+1，task依次num-1.任务都完成时任务结束。


# 1.创建一个 Queue.Queue() 的实例，然后使用数据对它进行填充。
# 2.将经过填充数据的实例传递给线程类，后者是通过继承 threading.Thread 的方式创建的。
# 3.每次从队列中取出一个项目，并使用该线程中的数据和 run 方法以执行相应的工作。
# 4.在完成这项工作之后，使用 queue.task_done() 函数向任务已经完成的队列发送一个信号。
# 5.对队列执行 join 操作，实际上意味着等到队列为空，再退出主程序。


def queue_basic_example():

	class ConsumerThread(th.Thread):
		"""从队列中获取数据"""

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
				print(f"pid:{self.index} process:{item} ...")
				self.queue.task_done()  # task_done 方法是未完成的任務數量 -1

	# 初始化函数接受一个数字来作为该队列的容量，如果传递的是
	# 一个小于等于0的数，那么默认会认为该队列的容量是无限的.
	q = queue.Queue(10)

	for idx in range(2):
		thread_i = ConsumerThread(idx, q)  # 2個線程同時處理隊列中的消息, 2 个消费者子线程
		thread_i.start()

	for i in range(10):  # 主线程模擬向隊列中賽數據
		q.put(i)
		time.sleep(2)

def queue_taskdone_test():
	"""
	https://blog.csdn.net/qq_43030934/article/details/132755839
	生产者线程可以调用 join() 阻塞
	消费者每处理完一条消息调用一次 task_done(), 队列中所有的消息处理完后, join() 接触阻塞
	"""
	def worker(idx, q):
		while True:
			item = q.get()
			print(f'worker {idx} process {item}')
			time.sleep(0.5)  # 模拟队列处理耗时
			q.task_done()

	q = queue.Queue()

	for i in range(5):
		q.put(i)

	# 创建 3 个线程
	for idx in range(3):
		t = threading.Thread(target=worker, args=(idx, q))
		t.daemon = True
		t.start()

	q.join()  # 阻塞等待处理结束
	print(f'all item process done, main thread exit')

def queue_task_done_example2():
	"""
	任务完成时通知使用
	入队的速度比出队快保证了 task_done() 通知收到的时候, 所有的任务都完成了
	"""
	def consumer(q):
		while True:
			item = q.get()
			print(f'get item:{item}')
			time.sleep(1)
			print(f'item:{item} process done')
			q.task_done()

	def producer(q):
		for i in range(5):
			q.put(i+1)
			print(f'put item:{i+1}')
			time.sleep(0.5)

	def monitor(q):
		time.sleep(3)
		while True:
			if not q.empty():
				q.join()
			else:
				break
		print(f'all item finished')

	q = queue.Queue()
	t1 = threading.Thread(target=consumer, args=(q,), daemon=True)
	t2 = threading.Thread(target=producer, args=(q,), daemon=True)
	t3 = threading.Thread(target=monitor, args=(q,), daemon=True)
	t1.start()
	t2.start()
	t3.start()
	time.sleep(10)

if __name__ == '__main__':
	# queue_basic_example()
	# queue_taskdone_test()
	queue_task_done_example2()

