import urllib.request
import base64
import time
import os

#直接打开jandan.net/ooxx这个网址
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
    
#在jandan.net/ooxx网址中，寻找最新的页码
def get_page(url):
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a : b]

#返回被加密的网址，输入值为页面号
def get_url_str(value):
    #编码之前的字符串
    decode_str = str(time.localtime()[0]) + ('%02d' % time.localtime()[1]) + ('%02d' % time.localtime()[2]) + '-' + str(value)
    #编码之后的字符串
    utf8_str = decode_str.encode('utf-8')
    encode_str = base64.b64encode(utf8_str)
    url = 'http://jiandan.net/ooxx/' + str(encode_str).split('\'')[1] + '#comments'
    return url


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')

    while(a != -1):
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append(html[a + 9 : b + 4])
        else:
            b = a + 9
        a  =html.find('img src=', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open('http:' + each)
            f.write(img)


def download_mm(folder = 'ooxx'):
    if not os.path.exists(folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url))

    for i in range(page_num):
        page_url = get_url_str(page_num)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)
        page_num -= 1

if __name__ == '__main__':
    download_mm()
