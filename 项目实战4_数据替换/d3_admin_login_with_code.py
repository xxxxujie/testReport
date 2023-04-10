import unittest
import jsonpath
import requests
import json
from 项目实战3.common.excel import read_excel_dict
from unittestreport import ddt, list_data
from config.setting import Config
from helper import api

# 读取excel
items = read_excel_dict(Config.case_file, sheet_name="adminLogin")


@ddt
class TestAdminLogin(unittest.TestCase):
    # 前置条件
    def setUp(self) -> None:
        """
        登录前置条件
        :return:
        """
        # 获取验证码图片
        pic = api.get_captcha()
        # 调用第三方平台，识别验证码
        self.code = api.get_code(uname="simple", pwd='yuan5311645', img=pic, typeid=3)

    @list_data(items)
    def test_01_admin_login(self, item):
        """测试步骤
        1、先要访问http://mall.lemonban.com:8108/captcha.jpg，得到验证码图片
        2、调用第三方的验证平台，得到验证码文字
        3、访问登录接口，在接口参数当中加入验证码替换
        """
        # data = json.dumps(item['json'])
        data = json.loads(item['json'])
        # 修改验证码
        data['imageCode'] = self.code
        response = requests.request(method=item['method'],
                                    url=item['url'],
                                    data=data)

        # 断言
        # 得到的是字典
        try:
            content = response.json()
            content['msg'] = 'ok'
        except:
            content = response.text()  # Incorrect account or password
            # 将字符串转换成字典
            content = {"msg": content}

        expected = json.loads(item['expected'])
        for jp_expr, value in expected.items():
            actual = jsonpath.jsonpath(content, jp_expr)[0]
            self.assertEqual(actual, value)
