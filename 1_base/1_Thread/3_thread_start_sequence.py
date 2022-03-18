#縣城的執行順序是無序的，有操作系統進行調度的
import threading as t

def task():
	# 獲取當前縣城對象
	sub_thread = t.current_thread()
	print(sub_thread)

if __name__ == '__main__':
	for i in range(10):
		# 創建10個子線程
		sub_thread = t.Thread(target = task)
		sub_thread.start()
	
