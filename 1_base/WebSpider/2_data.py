from urllib import request as r
with r.urlopen('http://www.baidu.com') as f:
	data = f.read(100)
	data.decode('utf-8')
##
#eg2:下載一只貓
import urllib.request as r
response = r.urlopen('http://www.placekitten.com/g/500/600')
##這裏使用'utf-8'(bytes)格式，而不解析爲unicode格式，因爲保存的時候直接使用寫二進制的方式保存
cat_img = response.read()
#圖片存儲
with open('cat_500_600', 'wb') as f:
	f.write(cat_img)
