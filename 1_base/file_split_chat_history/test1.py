#目的：對A和B的對話，分別保存boy_1.txt,boy_2.txt,...girl_1.txt,girl_2.txt...
#且“=======”分割的內容，分別保存。
#step1:打開文件
#step2:
#判斷該行是否爲：“========”
#是：文件的分別保存操作
#否：字符串分割操作

f = open('/home/qz/Desktop/python/file_split_chat_history/chat_record.txt', 'r')

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
		file_name_boy = 'boy_' + str(count) + '.txt'
		file_name_girl = 'girl_' + str(count) + '.txt'

		boy_file = open(file_name_boy, 'w')
		girl_file = open(file_name_girl, 'w')

		boy_file.writelines(boy)
		girl_file.writelines(girl)		#將這個列表的值寫入相應文件

		boy_file.close()
		girl_file.close()

		boy = []
		girl = []
		count += 1

file_name_boy = 'boy_' + str(count) + '.txt'		#將最後一次循環的內容保存，因爲沒有‘======’就不會保存
file_name_girl = 'girl_' + str(count) + '.txt'

boy_file = open(file_name_boy, 'w')
girl_file = open(file_name_girl, 'w')

boy_file.writelines(boy)
girl_file.writelines(girl)		

boy_file.close()
girl_file.close()


f.close()

















