import multiprocessing as mp
import os
import time

# TODO:多线程 和 多进程 怎么选择的问题

# 創建進程對象
#p1 = p.Process()

# 啓動進程執行任務
# start(target, name, group)	# target 就是线程入口函数
#p1.shtart()

def sing(num, name):
	""" 进程入口函數 """
	print('sing thread\'s PID = %d' % os.getpid())
	print('sing thread\'s Parent PID = %d' % os.getppid())
	for i in range(num):
		print(name + ' singing ' + str(i))
		time.sleep(1)
	print('sing thread exit')

def dance(num, name):
	"""进程入口函數"""
	print('dance thread\'s PID = %d' % os.getpid())
	print('dance thread\'s Parent PID = %d' % os.getppid())
	"""縣城入口函數"""
	for i in range(num):
		print(name + ' dancinging ' + str(i))
		time.sleep(1)
	print('dance thread exit')

# 2.进程需要传递参数的时候，可以传 元组类型args(1,2,3) 或者字典类型 kwargs={"num":3}
# (1) 元組傳參:按照順序傳參
# (2) 字典傳參:按照鍵值分配參數

# 3.獲取進程的 PID(Process ID)
# os.getpid() # 獲取當前進程的 PID
# os.getppid() # 獲取父進程的 PID

# 4.注意
# 主進程默認會等待所有的子進程執行結束再結束，
# 需要的效果:子進程結束，所以子進程也結束


if __name__ == '__main__':
	print('main thread\' PID = %d' % os.getpid())
	args = (6, "Jordan")	# tuple
	kwargs = {"num":3, "name":"Jay Chou"}	# dictionary, 字典傳參的時候，要保證鍵值存在
	# 創建進程對象
	process1 = mp.Process(target=sing, args=args)	# 元組的成員會被順序傳入進程入口函數
	process2 = mp.Process(target=dance, kwargs=kwargs)
	process1.start()
	process2.start()
	print('main exit')



