import os
import time
import multiprocessing as mp
import _thread # 线程操作庫
import sys
# task:多進程，高並發的拷貝


def copy_file(file_name, source_dir, dest_dir):
	"""將文件從源文件夾拷貝到目標文件夾"""
	source_file_path = source_dir + "/" + file_name
	dest_file_path = dest_dir + "/" + file_name
	# 1.鏈接源文件和目標文件路徑
	# 2.打開源文件 和 目標文件
	# 3.循環對源文件中的每一個文件夾進行拷貝，效率比較低，可以使用多進程程的方式
	print("Process ID = %d" % (os.getpid()))
	with open(source_file_path, "rb") as source_file:
		with open(dest_file_path, "wb") as dest_file:
			while True:
				data = source_file.read(1024)
				# 判斷是否文件結尾
				if data:
					dest_file.write(data)
				else:
					break
	#with 不用關閉文件

if __name__ == '__main__':
	print('Primary thread ID = %d' % os.getpid())
	source_dir = "/home/qz/Desktop/python/Thread/data"
	dest_dir = "/home/qz/Desktop/python/Thread/data_copy"

	# 讀取所有文件
	file_list = os.listdir(source_dir)

	# 遍歷
	try:
		os.mkdir(dest_dir)
	except:
		print('File ' + dest_dir + ' exist.')

	
	# 一個文件夾創建一個縣城
	for file_name in file_list:
		#copy_file(file_name, source_dir, dest_dir)
		# 使用多進程拷貝, 創建子進程
		sub_process = mp.Process(target=copy_file, args=(file_name, source_dir, dest_dir))
		sub_process.start()








