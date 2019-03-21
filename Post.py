import requests
import webbrowser
param={"wd":"莫烦python"}
r=requests.get('http://www.baidu.com/s',params=param)
print(r.url)
webbrowser.open(r.url) #自动打开浏览器链接，非常有用

data={'firstname':'莫烦','lastname':'周'}

r=requests.post(
   'http://pythonscraping.com/pages/files/processing.php',
   data=data)
print(r.text)

#upload image，通过post提交照片

file={'uploadFile':open('./1.jpg','rb')}
r=requests.post(
    'http://pythonscraping.com/files/processing2.php',
    files=file)
print(r.text)

#Use post method to login to a website

payload={'username':'Morvan','password':'password'}
r=requests.post(
    'http://pythonscraping.com/pages/cookies/welcome.php',
    data=payload
)
print(r.cookies.get_dict())
r=requests.get(
    'http://pythonscraping.com/pages/cookies/profile.php',
    cookies=r.cookies
)
print(r.text)

session=requests.Session()
payload={'username':'Morvan','password':'password'}
r=session.post(
    'http://pythonscraping.com/pages/cookies/welcome.php',
    data=payload)
print(r.cookies.get_dict())
r=session.get(
    'http://pythonscraping.com/pages/cookies/profile.php'
    )
print(r.text)
