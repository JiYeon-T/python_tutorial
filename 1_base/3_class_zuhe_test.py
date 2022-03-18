class Cat:
	__id = '001'	#private attribute	
	##
	def __init__(self, gender = 'female'):
		self.gender = gender
	##
	def __repr__(self):
		return self.name + ',hello.'
	##	
	def setName(self, name):
		self.name = name
	##
	def show(self):
		print('Hai')
	##
	def getID(self):
		return self.__id
##
class Dog:
	def __init__(self, gender = 'male'):
		self.gender = gender
	def hash(self):
		print('Wang, wang, wang.')
##
class Animal():
	def __init__(self, x, y):
		self.cat = Cat(x)
		self.dog = Dog(y)
	def print_gender(self):
		print("""cat's gender: %s, dog's gender: %s""" % (self.cat.gender, self.dog.gender))
##
a = Animal('female', 'male')
a.cat.show()
a.dog.hash()
a.print_gender()




