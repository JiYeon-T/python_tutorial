import time
import threading as t

#子縣城入口函數
def work():
	for i in range(3):
		print('workding...')
		time.sleep(1)

if __name__=='__main__':
	sub_thread = t.Thread(target=work)
	sub_thread.start()

	# 住縣城等待 1s 後結束
	# 默認會等待子線程結束在結束主線程
	print("Main thread end..")
	time.sleep(1)

	# 設置守護主線程
	# 主線程結束，子線程就自動銷毀
	#1daemon參數.work_thread = t.Thread(target=work, daemon=True)
	#2.work_thread.setDaemeon(True)
	#work_thread.start()
	
