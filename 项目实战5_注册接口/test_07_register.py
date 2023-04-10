"""
注册功能测试
前台商城：地址是不一样的，http://mall.lemonban.com:3344/    手工测试

测试流程：
1、输入手机号码，获取验证码，         /user/sendRegisterSms
请求方法：put
参数：{“mobile”:“11223456784”}
响应结果：“”

    验证码的验证逻辑
    1、点击发送验证码
    2、服务器生成一个验证码，随机数，发送给手机（会调用短信发送平台），验证码会被保存到服务器端
    具体保存到哪里，开发决定（mysql，redis，文件。。。。id，monile，validcode，createAt）
    3、用户输入验证码，请求校验验证码的接口        {"mobile":"11223456784","validCode":"2222"}
    url： put user/checkRegisterSms
    4、服务器通过用户传过来的mobile和validCode查询数据库，有没有记录，并且判断记录的值是否相等
    6、绑定手机和用户：put http://mall.lemonban.com:8107/user/registerOrBindUser

2、验证码从哪来
    1.手机短信，             不可取
    2.接口返回验证码？        不可取
    3.从测试数据库拿
"""
import json
import time
import unittest

import requests
from unittestreport import ddt, list_data
from faker import Faker
from helper import api
from common.db import DataBase
from config.setting import Config
from 项目实战5_注册接口.common.excel import read_excel_dict

items = read_excel_dict(Config.case_file, sheet_name='register')


@ddt
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 访问生成验证码接口
        # 生成随机的手机号
        fk = Faker(locale='zh_CN')
        mobile = fk.phone_number()
        api.send_sms_code(mobile)
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
        print(valid_code)
        # 校验 验证码接口
        self.flag = api.check_register_sms(mobile, valid_code=str(valid_code))
        self.mobile = mobile
        print(self.flag)

    @list_data(items)
    def test_login_01(self, item):
        # 注册
        # 反序列化
        # data = json.loads(item['json'])
        data = item['json']
        # 替换字符串数据
        data = data.replace('${flag}',self.flag)
        data = data.replace('${mobile}',self.mobile)
        url = Config.front_host+item['url']
        # 反序列化
        data = json.loads(data)
        result = requests.request(method=item['method'], url=url, json=data)
        print(result.text)
