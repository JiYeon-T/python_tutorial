# 自己定義一個容器（序列類型）
# 1,要求存放每個元素被訪問的次數（字典）
# 2，可以通過下標索引值；
class Vector(object):
	def __init__(self, *args):  # 可變參數
		self.values = [x for x in args]
		self.count = {}.fromkeys(range(len(self.values)), 0)  # 次數默認：0
		#fromkeys()對字典類型的數據初始化

	# 獲取容器長度
	def __len__(self):
		return len(self.values)

	# 獲取元素
	def __getitem__(self, key):
		self.count[key] += 1
		return self.values[key]

	# 對元素賦值
	def __setitem__(self, key, value):
		self.values[key] = value

	# 刪除元素
	def __delitem__(self, key):
		del self.values[key]

	##元素順序交換
	##def __reversed__(self):
	##contains()檢查
	def __contains__(self, item):
		for index in self.values:
			if index ==item:
				print('True')
				break
		else:
			print('False')
