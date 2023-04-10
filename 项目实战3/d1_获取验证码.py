import requests
import uuid


uid=str(uuid.uuid4())

param={'uuid':uid}
url='http://mall.lemonban.com:8108/captcha.jpg'
result=requests.request('get',url,params=param)
pic=result.content

with open('pic.png','wb') as f:
    f.write(pic)

