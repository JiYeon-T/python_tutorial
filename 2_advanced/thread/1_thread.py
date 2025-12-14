import threading as t  # 高級支持
import time
# import _thread  # 支持功能較少，一般不適用這個,主線程結束後，其他縣城自動結束等等很多不足
# 进程,线程,协程
# TODO: https://cloud.tencent.com/developer/article/2389367


def thread_basic_example1():
	def sing(name, num):
		"""@NOTE:元組方式傳參必須保證元組中元素的順序與形參順序一樣"""

		for ix in range(num):
			print(name + 'is singing... ' + str(ix))


	def dance(name, num):
		"""@NOTE:字典的key必須和任務的參數一樣，才可以使用字典類型傳參"""
		for ix in range(num):
			print(name + 'is dancing... ' + str(ix))

	singer = ("James", 3000)
	dancer = {'name': "Lebron", 'num': 4000}
	t1 = t.Thread(target=sing, args=singer)
	t2 = t.Thread(target=dance, kwargs=dancer)
	t1.start()
	t2.start()


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

	sub_thread = t.Thread(target=work)
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

if __name__ == '__main__':
	# thread_basic_example1()
	# daemon_thread_test()
	thread_running_sequence_test()