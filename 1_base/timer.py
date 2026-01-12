import time as t

class Timer:
	def __init__(self):
		self.unit = ['year', 'month', 'day', 'hour', 'minute', 'second']
		self.print_str = 'Not begin'	#string
		self.start_time = [0]		#list type
		self.stop_time = [0]
		self.last_time = [0]

	def __str__(self):
		return self.print_str

	__repr__ = __str__    # 重写 __repr__

	# add object: t1 + t2
	def __add__(self, other):  # 重写 __add__
		temp = 'All time is :'  # string, local varible temp
		add_result = []	 # list, save time sum
		for i in range(6):
			add_result.append(self.last_time[i] + other.last_time[i])
			temp += (str(add_result[i]) + self.unit[i])
		print(temp)

	# timer start
	def start(self):
		self.start_time = t.localtime()
		print('Timer started.')

	# timer stop
	def stop(self): 
		if not self.start_time:
			print('Please start ,Then stop.')
		else:
			self.stop_time = t.localtime()
			self._calc()	
			print('Timer stopped.')

	# inner function
	def _calc(self):
		self.last_time = []	
		self.print_str = 'Timer value is :'
		for i in range(6):
			self.last_time.append( self.stop_time[i] - self.start_time[i] )
			self.print_str += (str(self.last_time[i]) + self.unit[i])
		self.start_time = [0]
		self.stop_time = [0]

	#show style: 'xx year' + 'xx month' + ... + 'xx second'	
