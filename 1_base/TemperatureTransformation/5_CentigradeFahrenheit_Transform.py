##華氏溫度與攝氏溫度之間的轉換
##IPO-----(Input, Process(處理成數值 + 單位) ， Output)
def temperatureTransform():
	tempStr = input('請輸入攝氏度或者華氏度(C/F):')
	temp_symbol = tempStr[-1]	#最後一位
	temp_value = tempStr[0 : -1]	#分割數值和單位
	###
	if temp_symbol == 'F':
		changed_value = (float(temp_value) - 32) / 1.8
		changed_symbol = 'C'
		print('Changed value is:', changed_value, changed_symbol) 
	elif temp_symbol == 'C':
		changed_value = float(temp_value) * 1.8 + 32
		changed_symbol = 'F'
		print('Changed value is:', changed_value, changed_symbol) 
	else:
		print('Invalid input.')
###
if __name__ == '__main__':
	temperatureTransform()
