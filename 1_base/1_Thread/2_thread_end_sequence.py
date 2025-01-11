import time
import threading as t

#子线程入口函數
def work():
	for i in range(3):
		print('working...')
		time.sleep(1)

if __name__=='__main__':
	sub_thread = t.Thread(target=work)
	sub_thread.setDaemon(True) # 設置守護主線程,主線程結束，子線程就自動銷毀
	sub_thread.start()

	time.sleep(1) # 主线程等待 1s 後結束
	print("Main thread end..") # 默認主线程會等待子线程結束再結束

	# 设置为守护线程的方法:
	#1daemon參數.work_thread = t.Thread(target=work, daemon=True)
	#2.work_thread.setDaemeon(True)
	#work_thread.start()
	
