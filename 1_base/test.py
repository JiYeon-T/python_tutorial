###########################################
#import time as t
from time import localtime
##
class Timer:
	##
	def __str__(self):
		return str(self.last_time)
	__repr__ = __str__
	##
	def start(self):
		self.start_time = localtime()
	##add method
	def __add__(self, other):
		result = []
		for i in range(6):
			result.append(self.last_time[i] + other.last_time[i])
		print('all time is:' + str(result))
	##
	def stop(self):
		self.stop_time = localtime()
		self.calc()
	##
	def calc(self):
		self.last_time = []		# = {}
		for i in range(6):
			self.last_time.append( self.stop_time[i] - self.start_time[i] )
		print('all time is :' + str (self.last_time)) 
########## get the attribute
class C:
	def __getattribute__(self, name):
		print('__getattribute__')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('__getattr__')
		#super().__getattr__(name)
	def __setattr__(self, name, value):
		print('__setattr__')
		super().__setattr__(name, value)
	def __delattr__(self, name):
		print('__delattr__')
		super().__delattr__(name)

