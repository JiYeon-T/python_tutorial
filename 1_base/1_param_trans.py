

# 参数传递的核心问题在于：当函数内部对参数进行修改时，这些改动是否会影响到调用者提供的原始数据？
# 答案取决于传递的是数据的副本还是数据的引用。Python参数传递机制遵循“对象导向”原则，即一切皆对象，
# 参数传递实质上是对象的引用（或称为指针）的传递。理解这一关键点有助于我们深入探讨值传递与引用传递的区别。

# python 函数中的参数传递规则:取决于参数类型
# a.不可变类型(int, float, string, bool) , 创建副本并将该副本的引用传给函数, 内部修改不会影响原始变量
# b.可变类型(list, dict, 集合以及大多数自定义对象)，传递的事对象的引用，而非对象本身

# 综上所述，Python参数传递机制并非简单地归类为“值传递”或“引用传递” ，
# 而是基于数据类型的可变性来决定传递的是对象的副本引用还是原始对象引用。
# 理解这一特性对于编写高效、无副作用的Python代码至关重要

# https://cloud.tencent.com/developer/news/1356946

def param_trans_test():
	"""传参测试"""
	input_int = 20
	input_list = [123, 456]
	input_dic = {"id": 123}
	print(f"id:{id(input_int)}")
	print(f"id:{id(input_list)}")
	print(f"id:{id(input_dic)}")
	def copy_val(val):
		"""传递的都是引用具体传递引用还是拷贝取决于内部如何使用"""
		print(f"id:{id(val)} type:{type(val)} val:{val}") # 到这里还没变，和传入参数一致
		val = 1000
		# val[0] = 1000
		print(f"id:{id(val)} type:{type(val)} val:{val}") # 赋值操作后，val 的值是否变化取决于如何使用的
	def not_copy_val(val):
		"""参数是列表/字典等可变类型，但内部使用的参数确实是引用"""
		print(f"id:{id(val)} type:{type(val)} val:{val}")

	# copy_val((input_int))
	# copy_val(input_list)
	# copy_val(input_dic)
	not_copy_val((input_int))
	not_copy_val(input_list)
	not_copy_val(input_dic)

	print(input_list)
	print(input_dic)

def param_basic_op_test():
	val_int = 1
	def double(val):
		"""没有修改传入参数的原始值"""
		val *= 2
		return val
	print(f"res:{double(val_int)}", end=", ")
	print(f"input:{val_int}")

	val_text = "Hello"
	def append_text(text, suffix):
		"""没有修改传入参数的原始值"""
		text += suffix
		return text
	print(f"res:{append_text(val_text, ',world')}", end=", ")
	print(f"input:{val_text}")

	val_list = [1, 2, 3]
	def append_list(l, val):
		"""可变类型, 内部修改了传入的参数"""
		if not isinstance(l, list):
			return
		l.append(val)
		return l
	print(f"res:{append_text(val_list, [111, 222, 333])}", end=", ")
	print(f"input:{val_list} ")

	val_dict = {"USA":"The United States", "UK":"The United Kingdom",}
	def append_dict(d, k, v):
		"""传递引用"""
		if not isinstance(d, dict):
			return
		d[k] = v
		return d
	print(f"res:{append_dict(val_dict, 'CN', 'China')}")
	print(f"input:{val_dict} ")

# python 中的名称绑定与对象模型:
# 在Python中，变量赋值不仅仅是将一个值赋予一个名字那么简单。实际上 ，它涉及到一个重要的概念——名称绑定。
# Python采用“动态类型”和“对象模型”，其中每个变量名都充当一个引用，指向内存中的某个对象。
# 赋值过程就是将这个引用与指定的对象关联起来。
def object_mem_test():
	"""id()  is  == 的区别测试
	ython变量赋值的本质是建立名称与对象之间的绑定关系。
	通过id()、is与==的巧妙运用，我们可以深入洞察Python程序中变量与对象的交互，这对于理解和调试代码、避免不必要的错误具有重要意义
	"""
	# id()函数返回对象的唯一标识符，即对象在内存中的地址。
	# 对于可变对象 ，即使它们具有相同的值，只要它们是不同的实例，其id()也会不同。
	a = 10
	b = 10
	print(id(a), id(b), sep=",") # equal
	print(f"{a is b}  {a == b}")

	l1 = [1, 2, 3]
	l2 = l1.copy()
	print(id(l1), id(l2), sep=",") # unequal
	print(f"{l1 is l2}  {l1 == l2}")
	# 关键字is用于检查两个变量是否引用同一个对象。 与id()类似，它适用于判断对象身份而非值的等同性

	# 比较运算符==用于判断两个变量引用的对象是否具有相同的值。
	# 对于不可变类型，如果值相等，则通常意味着它们引用相同的对象
	# 而对于可变类型，即使值相等，也可能指向不同的对象

def copy_test():
	"""
	深拷贝与浅拷贝
	浅拷贝创建了一个新对象，但它只复制了原对象的第一层结构。
	对于嵌套的可变对象 ，浅拷贝仅复制顶层对象的引用 ，而不是底层对象。这可能导致意外的修改
	"""
	import copy
	original =[{"A":123, "B":456}, ] # list 中包含字典
	shallow_copy = copy.copy(original)
	print(original, shallow_copy, sep="  ")
	print(f"ori:{id(original)} shallow:{id(shallow_copy)}")
	shallow_copy[0]["A"] = 0 # 尽管创建了浅拷贝，但当修改原列表中字典的值时，浅拷贝中的对应项也随之改变。
	# original[0]["A"] = 0
	print(original, shallow_copy, sep="  ", end="\n\n")

	#  使用copy模块实现深拷贝
	# 为了解决浅拷贝的局限性 ，可以使用copy模块的deepcopy方法来创建一个完全独立的副本 ，包括所有层次的对象
	deep_copy = copy.deepcopy(original)
	print(f"ori:{original} deep:{deep_copy}")
	original[0]["A"] = 1000
	# deep_copy[0]["A"] = 1000
	print(original, deep_copy, sep="  ", end="\n\n")

	# 直接赋值是浅拷贝还是深拷贝呢??? -> 深拷贝
	# TODO: 研究一下这个，这不太合理。。。
	equal_op = original
	print(id(equal_op), id(original))
	print(f"ori:{original} =:{equal_op}")
	# original[0]["A"] = 2000
	equal_op[0]["A"] = 2000
	print(original, equal_op, sep="  ", end="\n\n")

def param_trans_test():
	"""
	Python参数传递的最佳实践
	"""
	# 列表推导式
	# lambda 表达式
	even_number = lambda x : x % 2 == 0
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(list(filter(even_number, numbers))) # filter() 返回的也是迭代器


if __name__ == '__main__':
	# param_trans_test()
	# param_basic_op_test()
	# copy_test()
	param_trans_test()