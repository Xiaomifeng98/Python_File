#Add the User-Agent

import urllib.request
import urllib.parse
import json
import time

while True:
    #delete the '_o'
    #url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    content = input('Input \'q!\' to exit this program.\nPlease input what you want to translate: ')
    if content == 'q!':
        break
    '''
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    '''

    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] =  'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15849608310833'
    data['sign'] = '7bfb509ed7918869a2626e1bf129cef5'
    data['ts'] = '1584960831083'
    data['bv'] = '70244e0061db49a9ee62d341c5fed82a'
    data['doctype'] = 'json'
    data['version'] ='2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'
    data = urllib.parse.urlencode(data).encode('utf-8')

    '''
    req = urllib.request.Request(url, data, head)
    '''

    req = urllib.request.Request(url, data)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36')

    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')

    target = json.loads(html)

    print('The result of the translation is: ' + target['translateResult'][0][0]['tgt'])
    time.sleep(5)

