##test1_openurl
import urllib.request # urllib是一個包（package_test）

def basic_url_test():
    response = openurl('https://www.baidu.com')
    ##解碼
    html = response.read()
    html = html.decode('utf-8')		#utf-8支持中文
    print(html)

if __name__ == '__main__':
    basic_url_test()