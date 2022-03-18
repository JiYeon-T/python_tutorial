##通過爬蟲寫一個字典，
##url:http://fanyi.youdao.com

##note:對字典類型數據的索引
dict1 = {'1':'a', '2':'b','list1':[{'3':'c', '4':'d'},{'5':'e', '6':'f'}], '6':'g', '8':'h'}
##索引
dict1['list1'][0]		#{'3': 'c', '4': 'd'}
dict1['list1'][0]['3']		#'c'
				#索引順序：由外向裏（字典->列表->字典）
#########################################################################################
import urllib.request as r
import urllib.parse as p
import json
##Request URL
##url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
##url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
##Form Data 字典類型
content = input("請輸入要翻譯的內容：")
data = {}
data['i'] = 'i love you'		##data['i'] = '我愛你'
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
##將data轉爲可以使用的類型-手冊，對urlopen(url, data)類型的需要
## It should be encoded to bytes before being used as the data parameter. ----<<urllib.request>>
##			   utf-8
data = p.urlencode(data).encode('utf-8')
##
response = r.urlopen(url, data)
html = response.read().decode('utf-8')
target = json.loads(html)			##字典類型
##
print(target['translateResult'][0][0]['tgt'])	##對字典類型中的翻譯內容進行索引

#############################################################################
##有道翻譯這裏獲取不到正確結果的原因是：有道翻譯2.1，要對cookies進行修改
##可以實現 -> 英譯漢
##url去掉_0,		不去的話報錯：err code: 50
########################################################################################
import urllib.request as r
import urllib.parse as p
import json
content = input("請輸入要翻譯的內容：")
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
##############################################################
##封裝____函數,模塊
#############################################################
##對於有反爬的網站，	方法一：headers{'User-Agent':''},模擬瀏覽器訪問
#############################################################
import urllib.request as r
import urllib.parse as p
import json
content = input("請輸入要翻譯的內容：")

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

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
'''
方法1:定義好headers
headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'
'''
##Request對象
request = r.Request(url, data)
##添加headers的方法2:Request.add_headers()
request = request.add_headers('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
##
response = r.urlopen(request)
html = response.read().decode('utf-8')
target = json.loads(html)
print(target['translateResult'][0][0]['tgt'])
#############################################################
##方法二：使用代理
#############################################################
import urllib.request as r
import random
##url = 'https://www.whatismyip.com'

url = 'http://45.32.164.128/ip.php'
'''
iplist = []
iplist.append('')
'''
proxy_support = r.ProxyHandler({'http':'119.57.108.73:53281'})
opener = r.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')]

r.install_opener(opener)

##response = opener.open(url)
##默認使用這個opener打開
response = r.urlopen(url)
html = response.read().decode('utf-8')
print(html)


#######################
##使用代理失敗-----------原因：connection refused.
###################



########################################################################################
##




































































































