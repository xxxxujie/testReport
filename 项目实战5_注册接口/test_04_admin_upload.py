import unittest

import requests

from 项目实战3.common.excel import read_excel_dict
from config.setting import Config
from unittestreport import ddt, list_data
from helper import api

# 读取excel
items = read_excel_dict(Config.case_file, sheet_name="adminLogin")


class TestAdminLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.token = api.admin_login()

    def test_01_admin_upload(self):
        # print(self.token)
        url = Config.admin_host+'/admin/file/upload/img'
        headers = {"Authorization":f"bearer{self.token}"}
        file = {"file":open('1.png','rb')}
        result=requests.request('post',url=url,headers=headers,files=file)
        print(result.text)

        self.assertTrue(".png" in result.text)