##迭代器(實際上就是擁有：__iter__和__next__方法的一個類)
class Fibs:
	def __init__(self, max = 10):
		self.a = 0
		self.b = 1
		self.max = max#max用來控制迭代次數
	def __iter__(self):
		return self
	def __next__(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > self.max:
			raise StopIteration#次數大於max跳出，不執行return
		return self.a

fib = Fibs(100)
try:
	for each in fib:
		print(each)
except StopIteration as reason:
	print('max')

##生成器
def Generator():
	print('生成器在執行...')
	yield 1
	yield 2
g = Generator
##next(g)
for i in g:
	print(i)

##eg:使用生成器計算fibonacci數列
def Fibs():
	a = 0
	b = 1
	while True:
		a, b = b, a+b
		yield a				#每次執行到這裏就停下，等待下一次迭代
						#使用for語句自動迭代
f = Fi
for i in f:
	if i > 100:
		break
	print(i)


