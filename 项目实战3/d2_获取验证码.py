import base64
import json

import requests
import uuid

uid=str(uuid.uuid4())

param={'uuid':uid}
url='http://mall.lemonban.com:8108/captcha.jpg'
result= requests.request('get',url,params=param)
pic=result.content


def base64_api(uname,pwd,img,typeid):

    base64_data=base64.b64encode(img)
    b64=base64_data.decode()
    data={"username":uname,"password":pwd,"typeid":typeid,"image":b64}
    result=json.loads(requests.post("http://api.ttshitu.com/predict",json=data).content)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


if __name__ == "__main__":
    result=base64_api(uname="simple",pwd='yuan5311645',img=pic,typeid=3)
    print(result)
