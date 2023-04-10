import string


data = """{"appType": 3, "checkRegisterSmsFlag": "${flag_o}",
        "mobile": "${mobile_o}", "userName": "${mobile_o}",
        "password": "1234", "registerOrBind": 1, "validateType": 1}"""

# replace
flag = 'qweqw'
mobile = '12344472834'

# data = data.replace('${flag}', flag)
# data = data.replace('${mobile}', mobile)
# print(data)

"""
新方法
"""

template = string.Template(data)
new_data = template.substitute(flag_o=flag,mobile_o=mobile)
print(new_data)

map = {"flag_o":flag,"mobile_o":mobile}
template = string.Template(data)
new_data = template.substitute(map)
print(new_data)