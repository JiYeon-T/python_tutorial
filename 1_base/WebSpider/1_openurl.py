##test1_openurl
import urllib.request as  r		##urllib是一個包（package）
response = openurl('http://www.aliali.online')
##解碼
html = response.read()
html = html.decode('utf-8')		#utf-8支持中文
print(html)
