import multiprocessing as p
import os
# 多线程 和 多进程 怎么选择的问题

# 創建進程對象
#p1 = p.Process()

# 啓動進程執行任務
# start(target, name, group)	# target 就是线程入口函数
#p1.shtart()

def sing(num, name):
	""" 进程入口函數 """
	print('sing thread\'s PID = %d' % os.getpid())
	print('sing thread\'s Parent process PID = %d' % os.getppid())
	for i in range(num):
		print(name + ' singing ' + str(i))

def dance(num, name):
	print('dance thread\'s PID = %d' % os.getpid())
	print('dance thread\'s Parent process PID = %d' % os.getppid())
	"""縣城入口函數"""
	for i in range(num):
		print(name + ' dancinging ' + str(i))	
# 2.进程需要传递参数的时候，可以传 元组类型args(1,2,3) 或者字典类型 kwargs={"num":3}
# (1) 元組傳參:按照順序傳參
# (2) 字典傳參:按照鍵值分配參數

# 3.獲取進程的 PID(Process ID)
# os.getpid()	# 獲取當前進程的 PID
# os.getppid()	# 獲取父進程的 PID

# 4.注意
# 主進程默認會等待所有的子進程執行結束再結束，
# 需要的效果:子進程結束，所以子進程也結束


if __name__ == '__main__':
	print('main thread\' PID = %d' % os.getpid())
	args = (1, "Jordan")	# tuple
	kwargs = {"num":1, "name":"Jay Chou"}	# dictionary, 字典傳參的時候，要保證鍵值存在
	# 創建進程對象
	p1 = p.Process(target=sing, args=args)	# 元組的成員會被順序傳入進程入口函數
	p2 = p.Process(target=dance, kwargs=kwargs)
	p1.start()
	p2.start()




