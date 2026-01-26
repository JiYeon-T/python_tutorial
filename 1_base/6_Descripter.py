##就是将某种特殊类(include one of __get__,__set__,__delete__)的实例，指派给另一个类的属性。
## The use of descriptor same like property() function,
##Therefore, We can write our own property function:
##		MyProperty() 
class MyDescriptor:
	##
	def __get__(self, instance, owner):
		print('getting', self, instance, owner)

	def __set__(self, instance, value):
		print('setting', self, instance, value)

	def __delete__(self, instance):			# bu neng yu del chong ming
		print('deleting',self, instance)


class Test:
	x = MyDescriptor()


test = Test()
test.x				#get
test.x = 'I love you'		#set --automaticlly call
del test.x			#del


##Define MyDescriptor()
class C:
	def __init__(self, x = 0):
		print('__init__ get called.')
		self._x = x			#私有成員
	def getX(self):
		return self._x
	def setX(self, value):
		 self._x = value
	def delX(self):
		del self._x
	##property()
	p = property(getX, setX, delX, 'Not Found.')

##test
class Test(object):
	cls_val = 1
	def __init__(self):
		self.ins_val = 10
t = Test()
print(Test.__dict__)
print('*' * 10)
print(t.__dict__)		##实例t的属性并不包含cls_val，cls_val是属于类Test的

##只要定義了get,set,delete方法中的一個就叫做————描述符
class Desc(object):
	def __get__(self, instance, owner):
		print('get')
		print('self = ', self)
		print('instance=', instance)
		print('owner=', owner)
		print('*' * 50)
	def __set__(self, instance, owner):
		print('get')
		print('self = ', self)
		print('instance=', instance)
		print('owner=', owner)
class Test(object):
	x = Desc()
test = Test()













































		
