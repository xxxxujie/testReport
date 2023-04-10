"""
业务相关的函数，访问接口的过程，访问每一个接口封装成一个函数
"""
import base64
import json
import uuid

import requests
from 项目实战5_注册接口.config.setting import Config


def get_captcha():
    """获取验证码"""
    uid = str(uuid.uuid4())
    param = {'uuid': uid}
    url = Config.admin_host+'/captcha.jpg'
    result = requests.request('get', url, params=param)
    return result.content


def get_code(img,uname=None, pwd=None, typeid=3):
    """识别验证码"""
    if uname is None:
        uname = Config.tujian_uname
    if pwd is None:
        pwd = Config.tujian_passwd
    base64_data = base64.b64encode(img)
    b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).content)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""


def admin_login(username=None,passwd=None):
    if username is None:
        username=Config.admin_username
    if passwd is None:
        passwd=Config.admin_passwd

    """管理员登录"""
    url = Config.admin_host+"/adminLogin"
    data = {"principal":username,"credentials":passwd,"imageCode":"lemon"}
    response=requests.request('post',url,json=data).json()
    return response['access_token']


def upload_img(token,file_path):
    """上传图片"""
    url = Config.admin_host+'/admin/file/upload/img'
    headers = {"Authorization":f"bearer{token}"}
    f = open(file_path,'rb')
    file = {"file":f}
    result=requests.request('post',url=url,headers=headers,files=file)
    f.close()
    return result.text


def send_sms_code(mobile):
    """发送手机验证码"""
    url = Config.front_host + '/user/sendRegisterSms'
    data = {"mobile":mobile}
    response=requests.request('put',url=url,json=data)
    return response.text


def check_register_sms(mobile,valid_code):
    """发送手机验证码"""
    url = Config.front_host+'user/checkRegisterSms'
    data = {"mobile":mobile,"validCode":valid_code}
    response = requests.request('put',url=url,json=data)
    return response.text
