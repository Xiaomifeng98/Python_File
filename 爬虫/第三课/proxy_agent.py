#还未成功
import urllib.request

url1 = 'http://myip.kkcha.com/'
url2 = 'https://www.ip.cn/'
url = url1
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'

proxy_support = urllib.request.ProxyHandler({'http' : '122.228.19.90:3389'})

opener = urllib.request.build_opener(proxy_support)

opener.open(url)


req = urllib.request.Request(url, headers = head)
response = urllib.request.urlopen(req)

html = response.read()

print(html)

