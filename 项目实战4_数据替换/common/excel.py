"""
common用来存储通用模块包
"""

import openpyxl
from openpyxl.worksheet.worksheet import Worksheet


def read_excel_dict(file,sheet_name="adminLogin"):
    workbook = openpyxl.load_workbook(file)
    # 获取表格，指定sheet变量类型
    sheet: Worksheet = workbook[sheet_name]
    rows = list(sheet.values)
    # 把列表当中每一个元素（元组）转换成一个字典
    # 1、对列表的每一个元素进行固定操作该用什么
    # 2、怎么把一个元组转换成一个字典
    # 三行测试数据
    cases = rows[1:]
    # 标题
    title = rows[0]
    lists = []
    lists2 = []
    for j in cases:
        for i in zip(title, j):
            lists.append(i)
        d1 = dict(lists)
        lists2.append(d1)
    print(lists2)
    # rows = [dict(zip(title, row) for row in cases)]
    return lists2