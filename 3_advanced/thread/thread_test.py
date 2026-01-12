import threading  # 高級支持
import time
# import _thread  # 支持功能較少，一般不適用這個,主線程結束後，其他縣城自動結束等等很多不足

# 进程,线程,协程
# TODO: https://cloud.tencent.com/developer/article/2389367
# https://www.runoob.com/python3/python3-multithreading.html

##########################################################################
# 1.threading
# threading基于Java的线程模型设计。
# 锁（Lock）和条件变量（Condition）在Java中是对象的基本行为（每一个对象都自带了锁和条件变量），
# 而在Python中则是独立的对象。
# Python Thread提供了Java Thread的行为的子集；没有优先级、线程组，线程也不能被停止、暂停、恢复、中断。
# Java Thread中的部分被 Python 实现了的静态方法在 threading 中以模块方法的形式提供。
# 创建方法:
# 方法1：直接使用 threading.Thread()创建线程，适用于线程简单的情况
# 使用：(1)多线程使用线程池的话通常使用这种方法;
# (2) 简单线程;
# 方法2：继承 Thread 实现多线程， 适用于线程复杂的时候
# 用法:  复杂线程时
# 重载 run 放法


def thread_basic_example1():
	def sing(name, num):
		"""@NOTE:元組方式傳參必須保證元組中元素的順序與形參順序一樣"""

		for ix in range(num):
			print(name + 'is singing... ' + str(ix))
			time.sleep(1)


	def dance(name, num):
		"""@NOTE:字典的key必須和任務的參數一樣，才可以使用字典類型傳參"""
		for ix in range(num):
			print(name + 'is dancing... ' + str(ix))
			time.sleep(1)

	singer = ("James", 3000)
	dancer = {'name': "Lebron", 'num': 4000}
	t1 = threading.Thread(target=sing, args=singer, name="singer")
	t2 = threading.Thread(target=dance, kwargs=dancer, name="dancer")
	t1.start()
	t2.start()

	while True:
		time.sleep(2)
		thread_list = threading.enumerate() # 返回一个包含正在运行的线程的列表。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
		print(f"list:{thread_list}")
		thread = threading.active_count()  # 返回正在运行的线程数量，与 len(threading.enumerate()) 有相同的结果。


def daemon_thread_test():
	"""
	設置守護主線程,主線程結束，子線程就自動结束,
	如果不设置, 会出现主线程结束, 但是子线程仍然在运行的情况
	设置为守护线程的方法:
	1. daemon參數.work_thread = t.Thread(target=work, daemon=True)
	2. work_thread.setDaemeon(True)
	work_thread.start()
	"""

	#子线程入口函數
	def work():
		for i in range(5):
			print(f'child thread working {i}')
			time.sleep(1)

	sub_thread = threading.Thread(target=work)
	# 创建新线程， 不设置守护线程, 子线程不受控制， 主线程结束, 子线程还在自己跑
	#(1) Daemon 设置子线程为守护线程, 听主线程的话. 即主线程退出, 则子线程也退出.
	#(2) join() 主线程阻塞等待子线程结束, 然后自己再结束
	sub_thread.setDaemon(True)  # 設置守護主線程,主線程結束，子線程就自動銷毀,
	sub_thread.start()

	time.sleep(1) # 主线程等待 1s 後結束
	print("Main thread end..") # 默認主线程會等待子线程結束再結束

def thread_running_sequence_test():
	"""
	线程的執行順序是無序的，由操作系統進行調度的
	"""

	def task(*args):
		# 獲取當前縣城對象
		sub_thread = t.current_thread()
		print("i:%d pid:%d running" % (i, sub_thread.native_id))

	for i in range(20):  # 創建10個子線程
		sub_thread = t.Thread(target=task, args=(i,))
		sub_thread.start()


#########################################################################
# 2._thread 模块
# _thread 提供了低级别的、原始的线程以及一个简单的锁。
# _thread 还提供了一个 ThreadLocal 类用于管理线程相关的数据，名为 thread._local，threading中引用了这个类。
# 由于 _thread 提供的线程功能不多，无法在主线程结束后继续运行，不提供条件变量等等原因，一般不使用 _thread 模块，

# _thread 对于进程何时退出没有任何控制。当主线程结束时，所有其他线程也都强制结束。不会发出警告或者进行适当的清理。
# 因而 python 多线程一般使用较为高级的 threading 模块，它提供了完整的线程控制机制以及信号量机制。
# TODO:但是这些 event, condition, semaphore 都具体是怎么控制的呢?


def _thread_test():
	"""_thread 模块测试"""

	import _thread
	import time

	def thread_entry():
		""" 线程入口函数 """
		for ix in range(1000):
			print(ix)
			time.sleep(1)
		print("线程结束")
		_thread.exit()  # 结束当前线程

	# 创建线程
	th1 = _thread.start_new_thread(thread_entry, (), {})  # 传入元组与字典这两个参数
	print(f"thread id:{_thread.get_ident()}")  # 不是线程 ID, 只是一个魔法数字
	_thread.interrupt_main() # 子线程中结束主线程， raise a KeyBoardInterrupt to interrupt main thread
	lock = _thread.allocate_lock()
	print("lock state:", lock.locked())
	count = 0  # 通过锁控制对全局变量的访问
	if lock.acquire():
		count += 1
		lock.release()
	# _thread 模块提供的线程都将在主线程结束后同时结束


if __name__ == '__main__':
	thread_basic_example1()
	# daemon_thread_test()
	# thread_running_sequence_test()
	# _thread_test()