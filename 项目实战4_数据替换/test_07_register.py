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
import unittest
from helper import api


class TestLogin(unittest.TestCase):
    def setUp(self):
        # 访问生成验证码接口
        mobile = '11223456784'
        api.send_sms_code("11223456784")
        # 获取验证码，操作数据库
        valid_code=''
        # 校验 验证码接口
        api.check_register_sms(mobile,valid_code=valid_code)

    def test_login_01(self):
        # 注册
        pass