import unittest
import requests

from 项目实战1.common.excel import read_excel_dict
from unittestreport import ddt,list_data

# 读取excel
fspath = r"D:\pythonWorkList\APITest\项目实战1\data\cases.xlsx"
items = read_excel_dict(fspath,sheet_name="adminLogin")


@ddt
class TestAdminLogin(unittest.TestCase):
    @list_data(items)
    def test_01_admin_login(self,item):
        response = requests.request(method=item['method'],url=item['url'],data=eval(item['json']))

        # 断言
        self.assertTrue("access_token" in response.text)

