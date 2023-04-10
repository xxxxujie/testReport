import string

from faker import Faker


# def replace_data(data, **kw):
#     """替换数据"""
#     template = string.Template(data)
#     data = template.substitute(**kw)
#     return data


def replace_data(data, map):
    """替换数据
    map:{"flag":'xxx',"mobile":'xxx'}
    """
    template = string.Template(data)
    data = template.substitute(map)
    return data


def generate_mobile():
    """生成手机号码"""
    fk = Faker(locale='zh_CN')
    mobile = fk.phone_number()
    return mobile

if __name__ == '__main__':
    data = 'hello ${a} world'
    new_data = replace_data(data, {"a": "along"})
    print(new_data)
