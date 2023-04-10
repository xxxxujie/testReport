import unittest

import jsonpath
import requests
import json

from 项目实战1.common.excel import read_excel_dict
from unittestreport import ddt, list_data
from config.setting import Config

# 读取excel
# fspath = r"D:\pythonWorkList\APITest\项目实战1\data\cases.xlsx"
items = read_excel_dict(Config.case_file, sheet_name="adminLogin")


@ddt
class TestAdminLogin(unittest.TestCase):
    @list_data(items)
    def test_01_admin_login(self, item):
        # 兼容性更强
        data = json.dumps(item['json'])
        response = requests.request(method=item['method'],
                                    url=item['url'],
                                    data=data)

        # 断言
        # 得到的是字典
        try:
            content = response.json()
            content['msg']='ok'
        except:
            content = response.text()   # Incorrect account or password
            # 将字符串转换成字典
            content = {"msg":content}

        expected = json.loads(item['expected'])
        # self.assertTrue(content['msg'] == 'Incorrect account or password')
        # self.assertTrue(content['token_type'] == 'bearer')
        # self.assertTrue(item['expected'] in response.text)
        for jp_expr,value in expected.items():
            # key: $..token_type
            # 预期结果：value
            # 实际结果：jsonpath.jsonpath(content,jp_expr)[0]
            actual=jsonpath.jsonpath(content,jp_expr)[0]
            self.assertEqual(actual,value)
            # self.assertTrue(content[jp_expr] == value)


