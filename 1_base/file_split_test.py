
def chat_file_split_test1():
	f = open('/home/qz/Desktop/pyhon/chat_record.txt', 'r')
	boy = []
	girl = []
	count = 1
	for each_line in f:
		if each_line[:6] == '======':
			file_name_boy = 'boy_' + str[count] + '.txt'
			file_name_girl = 'girl_' + str[count] + '.txt'

			boy_file = open('file_name_boy', 'w')		#This action will create a new txt 									file
			girl_file = open('file_name_girl', 'w')

			boy_file.writelines(boy)
			girl_file.writelines(girl)

			boy_file.close()
			girl_file.close()

			boy = []
			girl = []  # boy.clear(),girl.clear()
			count += 1

		else:
			(role, role_says) = each_line.split(':', )  #this is chat history, not split signal

			if role == 'A':
				boy.append(role_says)
			if role == 'B':
				girl.append(role_says)
	f.close()

def chat_file_split_test2():
	"""把test1重復的地方封裝成函數，使得函數變得簡潔明了"""
	def save_file(boy_msg, girl_msg, count):
		"""重復的部分封裝成函數，保存函數"""
		file_name_boy = 'boy_' + str(count) + '.txt'
		file_name_girl = 'girl_' + str(count) + '.txt'

		boy_file = open(file_name_boy, 'w')
		girl_file = open(file_name_girl, 'w')

		boy_file.writelines(boy_msg)
		girl_file.writelines(girl_msg)  # 將這個列表的值寫入相應文件

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
				(person, person_spoken) = each_line.split(':', 1)  # 字符串分割
				if person == 'A':
					boy.append(person_spoken)
				if person == 'B':
					girl.append(person_spoken)
			else:
				save_file(boy, girl, count)
				boy = []
				girl = []
				count += 1

		save_file(boy, girl, count)  # 將最後一次循環的內容保存，因爲沒有‘======’就不會保存

		f.close()


	split_file('/home/qz/Desktop/python/file_split_chat_history/chat_record.txt')  # split_file函數調用

if __name__ == '__main__':
	chat_file_split_test1()
