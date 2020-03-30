import urllib.request
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('user-agent' , 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')
    return html

def get_iport(html):
    ip = r'(?:(?:[0,1]?\d?\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[0,1]?\d?\d)'
    ip_list = re.findall(ip, html)

    port = r'<td>(\d+)</td>'
    port_list = re.findall(port, html)

    ip_info = []
    for i in range(0, 100):
        ip_info.append(str(ip_list[i]) + ':' + str(port_list[i]))
    return ip_info

if __name__ == '__main__':
    url = 'https://www.xicidaili.com/nn'
    get_iport(open_url(url))
