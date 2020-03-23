import urllib.request
import urllib.parse
import json

#delete the '_o'
#url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

content = input('Please input what you want to translate: ')

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

response = urllib.request.urlopen(url, data)
html = response.read().decode('utf-8')

target = json.loads(html)

print('The result of the translation is: ' + target['translateResult'][0][0]['tgt'])
