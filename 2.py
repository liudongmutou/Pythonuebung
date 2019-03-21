import requests
IMAGE_URL='http://pic1.16xx8.com/allimg/170801/1-1FP116442T62.jpg'
r=requests.get(IMAGE_URL,stream=True)

with open('.Desktop/image4.png','wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
