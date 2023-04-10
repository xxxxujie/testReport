"""
faker pip install faker
"""

from faker import Faker

# 生成一个手机号码
fk = Faker(locale='zh-CN')
phone = fk.phone_number()
print(phone)
# 名字
print(fk.name())
# 地址
print(fk.address())
# 公司
print(fk.company())
# 身份证号码
print(fk.ssn())
print(fk.job())

print(fk.profile())