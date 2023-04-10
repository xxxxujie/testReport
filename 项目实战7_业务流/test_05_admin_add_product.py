import json
import unittest

import requests

from 项目实战3.common.excel import read_excel_dict
from config.setting import Config
from unittestreport import ddt, list_data
from helper import api

# 读取excel
items = read_excel_dict(Config.case_file, sheet_name="addProduct")


@ddt
class TestAdminLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.token = api.admin_login()
        self.pic_path=api.upload_img(self.token,"2.png")

    @list_data(items)
    def test_01_admin_upload(self,item):
        # 上传产品
        headers = {"Authorization":f"bearer{self.token}"}
        data = json.loads(item['json'])
        data['pic'] = self.pic_path
        data['img'] = self.pic_path
        result = requests.request(item['method'],url=Config.admin_host+item['url'],headers=headers,json=data)
        print(result.text)

