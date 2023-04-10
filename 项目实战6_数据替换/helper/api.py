"""
业务相关的函数，访问接口的过程，访问每一个接口封装成一个函数
"""
import base64
import json
import time
import uuid

import requests
from faker import Faker

from 项目实战5_注册接口.config.setting import Config
from 项目实战6_数据替换.common import util
from 项目实战6_数据替换.common.db import DataBase


def get_captcha():
    """获取验证码"""
    uid = str(uuid.uuid4())
    param = {'uuid': uid}
    url = Config.admin_host + '/captcha.jpg'
    result = requests.request('get', url, params=param)
    return result.content


def get_code(img, uname=None, pwd=None, typeid=3):
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


def admin_login(username=None, passwd=None):
    if username is None:
        username = Config.admin_username
    if passwd is None:
        passwd = Config.admin_passwd

    """管理员登录"""
    url = Config.admin_host + "/adminLogin"
    data = {"principal": username, "credentials": passwd, "imageCode": "lemon"}
    response = requests.request('post', url, json=data).json()
    return response['access_token']


def upload_img(token, file_path):
    """上传图片"""
    url = Config.admin_host + '/admin/file/upload/img'
    headers = {"Authorization": f"bearer{token}"}
    f = open(file_path, 'rb')
    file = {"file": f}
    result = requests.request('post', url=url, headers=headers, files=file)
    f.close()
    return result.text


def get_sms_code(mobile):
    """发送手机验证码"""
    url = Config.front_host + '/user/sendRegisterSms'
    data = {"mobile": mobile}
    response = requests.request('put', url=url, json=data)
    # 等待一段时间后再查寻
    time.sleep(3)
    # 获取验证码，操作数据库
    db = DataBase(
        **Config.db
    )
    sql = f'select mobile_code from yami_shops.tz_sms_log where user_phone={mobile} order by id desc limit 5'
    valid_code = db.query_one(sql)['mobile_code']
    # 读取完之后要关掉
    db.close()
    return valid_code


def check_register_sms(mobile, valid_code):
    """发送手机验证码"""
    url = Config.front_host + '/user/checkRegisterSms'
    data = {"mobile": mobile, "validCode": valid_code}
    response = requests.request('put', url=url, json=data)
    return response.text


class APICase:
    def get_captcha(self):
        """获取验证码"""
        uid = str(uuid.uuid4())
        param = {'uuid': uid}
        url = Config.admin_host + '/captcha.jpg'
        result = requests.request('get', url, params=param)
        return result.content

    def get_code(self, img, uname=None, pwd=None, typeid=3):
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

    def admin_login(self, username=None, passwd=None):
        if username is None:
            username = Config.admin_username
        if passwd is None:
            passwd = Config.admin_passwd

        """管理员登录"""
        url = Config.admin_host + "/adminLogin"
        data = {"principal": username, "credentials": passwd, "imageCode": "lemon"}
        response = requests.request('post', url, json=data).json()
        return response['access_token']

    def upload_img(self, token, file_path):
        """上传图片"""
        url = Config.admin_host + '/admin/file/upload/img'
        headers = {"Authorization": f"bearer{token}"}
        f = open(file_path, 'rb')
        file = {"file": f}
        result = requests.request('post', url=url, headers=headers, files=file)
        f.close()
        return result.text

    def get_sms_code(self, mobile):
        """发送手机验证码"""
        url = Config.front_host + '/user/sendRegisterSms'
        data = {"mobile": mobile}
        response = requests.request('put', url=url, json=data)
        # 等待一段时间后再查寻
        time.sleep(3)
        # 获取验证码，操作数据库
        db = DataBase(
            **Config.db
        )
        sql = f'select mobile_code from yami_shops.tz_sms_log where user_phone={mobile} order by id desc limit 5'
        valid_code = db.query_one(sql)['mobile_code']
        # 读取完之后要关掉
        db.close()
        return valid_code

    def check_register_sms(self, mobile, valid_code):
        """发送手机验证码"""
        url = Config.front_host + '/user/checkRegisterSms'
        data = {"mobile": mobile, "validCode": valid_code}
        response = requests.request('put', url=url, json=data)
        return response.text

    def generate_mobile(self):
        """生成手机号码"""
        return util.generate_mobile()

    def replace_data(self, data, map):
        """数据替换"""
        return util.replace_data(data, map)

    def send_http(self, method, url, json=None, headers=None, data=None, **kw):
        response = requests.request(method=method, url=url, json=json, headers=headers, data=data, **kw)
        try:
            return response.json()
        except:
            content = response.text
            return {'err_msg': content}

    def api_automation(self,item,map):
        """
        item:{"id":"","title":"","url":"","json":"","headers":""}
        :param item:
        :return:
        """
        # 第一步：数据预处理
        method = item['method']
        url:str = item['url']
        # 如果url 用http开头，那就不拼接；如果没有，就拼接host
        if not url.startswith('http'):
            url = Config.front_host+url
        # json
        json_data = item['json']
        # 先用replace_data 把新数据替换进来，然后再转成字典
        # TODO：动态的数据替换
        json_data = self.replace_data(json_data,map)
        # 反序列化
        json_data = json.loads(json_data)

        headers = item.get('headers',None)
        data = item.get('data',None)
        # 发送请求
        response = self.send_http(method=method,url=url,json=json_data,headers=headers,data=data)
        return response
        # 第二步：