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
		girl = []		#boy.clear(),girl.clear()
		count += 1

	else:
		(role, role_says) = each_line.split(':', )  #this is chat history, not split signal
							#get a list
		if role == 'A':
			boy.append(role_says)
		if role == 'B':
			girl.append(role_says)

