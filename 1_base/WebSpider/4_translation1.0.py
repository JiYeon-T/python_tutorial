import urllib.request as r
import urllib.parse as p
import json
import time
while True:
	content = input("請輸入要翻譯的內容(輸入'q!'退出程序)：")
	if content == 'q!':
		break
	data = {}
	data['i'] = content
	data['from'] = 'AUTO'
	data['to'] = 'AUTO'
	data['smartresult'] = 'dict'
	data['client'] = 'fanyideskweb'
	data['salt'] = '15862206506111'
	data['sign'] = 'bbb0396a78da2a1f1ce426b91694f673'
	data['ts'] = '1586220650611'
	data['bv'] = '53c27a632bf14e8d71edd04ff664f211'
	data['doctype'] = 'json'
	data['version'] = '2.1'
	data['keyfrom'] = 'fanyi.web'
	data['action'] = 'FY_BY_CLICKBUTTION'
	data = p.urlencode(data).encode('utf-8')
	url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
	response = r.urlopen(url, data)
	html = response.read().decode('utf-8')
	target = json.loads(html)
	print(target['translateResult'][0][0]['tgt'])
	time.sleep(5)
##############################################################
##封裝____函數,模塊

'''def test():
	pass

if __name__ == '__main__':
	test()'''
