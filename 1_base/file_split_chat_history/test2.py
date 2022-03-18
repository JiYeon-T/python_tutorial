##把test1重復的地方封裝成函數，使得函數變得簡潔明了

def save_file(boy, girl, count):
	"""重復的部分封裝成函數，保存函數"""
	file_name_boy = 'boy_' + str(count) + '.txt'
	file_name_girl = 'girl_' + str(count) + '.txt'

	boy_file = open(file_name_boy, 'w')
	girl_file = open(file_name_girl, 'w')

	boy_file.writelines(boy)
	girl_file.writelines(girl)		#將這個列表的值寫入相應文件

	boy_file.close()
	girl_file.close()


def split_file(file_name):
	"""這個也封裝成函數，把聊天記錄分隔成爲兩部分"""
	f = open(file_name)

	boy = []
	girl = []
	count = 1

	for each_line in f:
		if each_line[:6] != '======':
			(person, person_spoken) = each_line.split(':', 1)	#字符串分割
			if person == 'A':
				boy.append(person_spoken)
			if person == 'B':
				girl.append(person_spoken)
	
		else:
			save_file(boy, girl, count)

			boy = []
			girl = []
			count += 1

	save_file(boy, girl, count)		#將最後一次循環的內容保存，因爲沒有‘======’就不會保存

	f.close()

split_file('/home/qz/Desktop/python/file_split_chat_history/chat_record.txt')		#split_file函數調用
