import urllib.request
import urllib.parse
import json

content=input("请输入需要翻译的内容：")

url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule&sessionFrom='

head={}
head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
data={}

data['i']='love'
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='1511796087630'
data['sign']='cf50fea6491a15229675d4d50fd101ca'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'
data=urllib.parse.urlencode(data).encode('utf-8')

req=urllib.request.Request(url,data)
req.add_header('User-Agent',head)
response=urllib.request.urlopen(req)
html=response.read().decode('utf-8')


target=json.loads(html)
print(target["translateResult"][0][0]["tgt"])




