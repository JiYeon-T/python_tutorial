import os
import time
import multiprocessing as mp
# 4.注意
# 主進程默認會等待所有的子進程執行結束再結束
# 需要的效果:主進程結束，所以子進程也結束

# 1. 設置守護主進程，
# process.daemon = True
# daemon 設置爲 True 以後，主進程不在等待子進程執行結束,直接結束，不在等待子進程

def work():
	#子進程工作2s
	for i in range(10):
		print('process1 running...')
		time.sleep(1)
	print('子進程執行結束')

if __name__ == '__main__':
	work_process = mp.Process(target=work)
	work_process.daemon = True # 設置爲 True 以後，主進程不再等待子進程執行結束, 默认 False
	work_process.start()

	time.sleep(1) # 主進程睡眠1s
	print('主進程執行結束')	# 這裏主進程不會立即結束，而是要等待子進程結束



