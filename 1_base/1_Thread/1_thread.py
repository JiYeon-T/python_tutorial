import threading as t	#高級支持
#import _thread		#支持功能較少，一般不適用這個,主線程結束後，其他縣城自動結束等等很多不足
# 进程,线程,协程
# TODO: https://cloud.tencent.com/developer/article/2389367


def sing(name, num):
	"""@NOTE:元組方式傳參必須保證元組中元素的順序與形參順序一樣"""
	for ix in range(num):
		print(name + ' singing... ' + str(ix) )

def dance(name, num):
	"""@NOTE:字典的key必須和任務的參數一樣，才可以使用字典類型傳參"""
	for ix in range(num):
		print(name + ' dancing... ' + str(ix))


if __name__ == '__main__':
	singer = ("James", 3000)
	dancer = {'name':"Lebron", 'num':4000}
	t1 = t.Thread(target=sing, args=singer)
	t2 = t.Thread(target=dance, kwargs=dancer)
	t1.start()
	t2.start()
