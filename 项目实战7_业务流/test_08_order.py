"""
15816236473
下单功能
1、登录 POST /login   {"principal":"15816236473","credentials":"1234","appType":3,"loginType":0}
2、有个商品 GET /prod/prodInfo?prodId=16938
3、选择购买的商品、颜色、SKU、下单
4、确认订单 /p/order/confirm
{"addrId":0,"orderItem":{"prodId":16938,"skuId":17299,"prodCount":1,"shopId":1},"couponIds":[],"isScorePay":0,"userChangeCoupon":0,"userUseScore":0,"uuid":"d595d1d9-8c5d-4cb1-8f96-5de390a41608"}
5、提交订单
{"orderShopParam":[{"remarks":"","shopId":1}],"uuid":"d595d1d9-8c5d-4cb1-8f96-5de390a41608"}
6、付款
post http://mall.lemonban.com:8107/p/order/pay
{"payType":2,"orderNumbers":"1641374519992258560"}

weixin://wxpay/bizpayurl?pr=YQuRm6uzz
"""
import unittest

from unittestreport import ddt, list_data

from 项目实战7_业务流.common.excel import read_excel_dict
from 项目实战7_业务流.config.setting import Config
from 项目实战7_业务流.helper.api import APICase

items = read_excel_dict(Config.case_file, sheet_name='pay')


@ddt
class TestRegister(unittest.TestCase, APICase):
    def setUp(self):
        # 登录
        token = self.login(Config.admin_username,Config.admin_passwd)
        # 获取商品
        skuId = self.get_product(16938)
        # 确认订单
        self.confirm_order(token,16938,skuId)
        # 提交订单
        orderNumber = self.submit_order(token)
        self.map = {"orderNumber":orderNumber}
        pass

    @list_data(items)
    def test_login_01(self, item):
        # 付款
        self.api_automation(item,self.map)
        pass
