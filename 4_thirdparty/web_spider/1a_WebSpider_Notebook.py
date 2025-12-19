##1.處理訪問異常的兩種方法
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
someurl = 'http://www.alila-fox.com'
req = Request(someurl)
try:
	response = urlopen(req)
except HTTPError as e:
	print('The server couldn\'t fulfill the request.')
	print('error code:', e.code)
	print('error reason:', e.reason)
except URLError as e:
	print('Failed to reach the server.')
	print('Error reason:', e.reason)
else:
	print('Everything is OK.')

###########################################################################
##key2:通過判斷錯誤的原因擁有的屬性來判斷是客戶端的問題還是服務器端的問題：
##(1)有reason，client的問題
##(2)有code,server的問題（返回的錯誤碼）
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
someurl = 'http://www.aliali.online'
req = Request(someurl)
try:
	response = urlopen(req)
except URLError as e:
	if hasattr(e, 'reason'):
		print('Failed to reach the server.')
		print('Error reason:', e.reason)
	elif hasattr(e, 'code'):
		print('The server couldn\'t ')
		print('Error code:', e.code)
else:
	print('Everything is OK.')
##everything is OK,do the next operation.

















