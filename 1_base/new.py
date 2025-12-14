class MyProperty:
	##
	def __init__(self, fget = None, fset = None, fdel = None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
	##rewrite __get__	
	def __get__(self, instance, owner):
		return self.fget(instance)
	##
	def __set__(self, instance, value):
		self.fset(instance, value)
	##
	def __delete__(self, instance):
		self.fdel(instance)
##
class C:
	def __init__(self):
		self.x = None
	def getX(self):
		return self.x
	def setX(self, value):
		self.x = value
	def delX(self):
		del self.x
	x = MyProperty(getX, setX, delX)

# eg:  # accomplish a temperature test with 'descriptor'
class Temperature:
	clus = Clusius()
