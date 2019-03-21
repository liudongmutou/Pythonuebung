import os
os.makedirs('./img/',exist_ok=True)

IMAGE_URL='https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'

from urllib.request import urlretrieve
urlretrieve(IMAGE_URL,'.Desktop/image1.png') #retrieve是取过来的意思

#request download

import requests
MAGE_URL='https://morvanzhou.github.io/static/img/description/learning_step_flowchart.png'
r=requests.get(IMAGE_URL)
with open('.Desktop/image2.png','wb') as f:      #wb,写的形式
    f.write(r.content)


r=requests.get(IMAGE_URL,stream=True)

with open('.Desktop/image3.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)


import requests
MAGE_URL='https://www.google.de/search?q=%E9%A3%8E%E6%99%AF%E7%85%A7&tbm=isch&tbo=u&source=univ&sa=X&ved#imgrc=dvaWgixuM-n-8M:'
r=requests.get(IMAGE_URL,stream=True)

with open('.Desktop/image4.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
