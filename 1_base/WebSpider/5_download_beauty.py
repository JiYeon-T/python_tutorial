##模塊化的變成思想————封裝
##下載圖片並且保存
#######還是有點問題，
######失敗
import os
import urllib.request

def url_open(url):
	req = urllib.request.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36')
	response = urllib.request.urlopen(req)
	html = response.read()
	'''
	這裏不解碼成'unicode'的原因是等等保存圖片直接寫二進制
	圖片無法轉換成爲'unicode'格式，始終'utf-8'(bytes格式)
	'''
	print(url)
	return html

def get_page(url):
	'''
	獲得最近一頁圖片的頁數號碼（例如,當前是：186），作爲返回值返回
	標籤中會有current_page，內容，查到到current-comment-page即可 	
	'''
	html = url_open(url).decode('utf-8')

	##解碼後查找'current-comment-page'字符即可,後面就是當前最新頁
	a = html.find('current-comment-page') + 23
	b = html.find(']', a)		#從a開始
	print(html[a:b])

	return html[a:b]		##返回的是一個字符串
	

def find_imgs(page_url):
	'''將該頁中所有圖片的url提取出來，保存在一個列表中'''
	html = url_open(page_url).decode('utf-8')
	img_address = []
	
	while a!= -1:
		a = html.find('img src=')
		b = html.find('.jpg', a, a + 255)		#從a開始，a+255結束，找不到返回：-1
		if b != -1:
			img_address.append(html[a+9 : b+4])
		else:
			b = a + 9
		##a找到，b也找到，a,從b的位置開始找，否則一直原地循環
		a = html.find('img src=', b)
	
	for each in img_address:
		print(each)

def save_imgs(img_address, folder):
	'''將圖片URL的列表中的所有圖片都保存————到制定的文件夾'''
	for each in img_address:
	'''使用'/'分割地址，返回列表，去列表最後一個元素作爲圖片名稱'''
		filename = each.split('/')[-1]
		with open(filename, 'wb') as f:
		img = urlopen(each)
		f.write(img)
		##返回圖片爲bytes類型，直接保存

def download_mm(folder = 'OOXX', pages = 10):
	##folder爲保存的文件夾名稱
	##pages要下載的頁碼個數
	os.mkdir(folder)
	os.chdir(folder)
	
	url = 'http://jandan.net/ooxx'
	page_num = int(get_page(url))
	
	for i in range(pages):
		'''每一頁的URL構成規律如下：僅僅是page數字不相同
		http://jandan.net/ooxx/page-186#comments'''
		page_num -= i
		page_url = url + '/page-' + str(page_num) + '#comments'
		img_address = find_imgs(page_url)
		save_imgs(img_address, folder)

if __name__ == '__main__':
	download_mm()









	





####不能使用代理，代理的節點服務器會加入廣告


