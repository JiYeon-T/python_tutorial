##property測試
class C:
	def __init__(self, size = 0, size2 = 0):
		self.size = size
		self.size2 = size2
	def getSize(self):
		return self.size
	def setSize(self, value):
		self.size = value
	def delSize(self):
		del self.size
	def getSize2(self):
		return self.size2
	def setSize2(self, value):
		self.size2 = value
	def delSize2(self):
		del self.size2
##使用這種方法可以將類的方法封裝起來：
	x = property(getSize, setSize, delSize, "I'm the 'x' property")
	y = property(getSize2, setSize2, delSize2, "I'm the 'y' property")
