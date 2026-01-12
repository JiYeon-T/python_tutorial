
## 迭代器(實際上就是擁有：__iter__和__next__方法的一個類)
def iterator_test():
	class Fibs:

		def __init__(self, max=10):
			self.a = 0
			self.b = 1
			self.max = max  # max用來控制迭代次數

		def __iter__(self):
			"""for 循环第一次进入时会调用该方法获取到迭代器对象"""
			print(f"iter get called")
			return self

		def __next__(self):
			"""每轮迭代都会调用到的方法"""
			print(f"next get called")
			self.a, self.b = self.b, self.a + self.b
			if self.a > self.max:
				raise StopIteration  # 次數大於max跳出，不執行return
			return self.a

	fib = Fibs(10)
	try:
		for each in fib:
			print(each)
	except StopIteration as reason:
		print('max')


def generator_test():
	##生成器
	def Generator():
		print('生成器在執行...')
		yield 1
		yield 2

	g = Generator
	next(g)
	# for i in g:
	# 	print(i)


def generator_test2():
	##eg:使用生成器計算fibonacci數列
	def Fibs():
		a = 0
		b = 1
		while True:
			a, b = b, a + b
			yield a  # 每次執行到這裏就返回a 并停下，等待下一次迭代

	# #使用for語句自動迭代
	f = Fibs()
	for i in f:
		if i > 10:
			break
		print(i, end=",")


if __name__ == '__main__':
	# iterator_test()
	# generator_test()
	generator_test2()