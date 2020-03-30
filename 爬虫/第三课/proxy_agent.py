#成功，但是ip地址会被屏蔽，自求多福
import urllib.request
import random

url1 = 'http://myip.kkcha.com/'
url2 = 'https://www.ip.cn/'
url = url1

iplist = ['106.14.173.173:8080', '117.62.173.23:8118', '59.172.27.6:53281', '1.202.116.62:8118', '121.237.149.188:3000']

proxy_support = urllib.request.ProxyHandler({'http' : random.choice(iplist)})

opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')]

urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)

html = response.read().decode('utf-8')

print(html)

