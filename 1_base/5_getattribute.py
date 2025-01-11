##屬性訪問的魔法方法
class C:
	"""class C's class document"""
	##對這些魔法方法進行重寫，但是不修改本來的功能
	def __getattribute__(self, name):
		"""__getattribute__()'s function document"""
		print('__getattribute__')
		return super().__getattribute__(name)
	def __getattr__(self, name):
		print('__getattr__')
	def __setattr__(self, name, value):
		print('__setattr__')
		return super().__setattr__(name, value)
	##__delattr__沒有返回值
	def __delattr__(self, name):
		print('__delattr__')
		super().__delattr__(name)
##Note:先調用__getattr__,當__getattr__沒有獲取到這個屬性時候，再調用__getattribute__
class Rectangle(object):
	def __init__(self, length = 0, width = 0):
		self.length = length		##觸發__setattr__
		self.width = width		
	def __setattr__(self, name, value):
		if name == 'square':
			self.width = value
			self.length = value
		else:
			## self.name = value
			#這裏出現無限遞歸,死循環
			super().__setattr__(name, value)
			self.__dict__[name] = value
	def getArea(self):
		return self.length * self.width


