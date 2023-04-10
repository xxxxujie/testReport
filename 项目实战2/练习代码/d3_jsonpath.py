import jsonpath

"""
jsonpath：指的是获取json指定字段的路径
"""
a_json = {
    "msg":"ok",
    "data":{
        "token_info":{
            "token":"abc",
            "token_type":"bearer"
        },
        "id":123,
        "name":"xujie"
    }
}

a = a_json["data"]["token_info"]["token_type"]
# 等同于 a_json["msg"]
result=jsonpath.jsonpath(a_json,expr='$.msg')
print(result)

# 获取data
data=jsonpath.jsonpath(a_json,expr='$.data')
print(data)

# 获取token_type
token_type=jsonpath.jsonpath(a_json,expr='$.data.token_info.token_type')
print(token_type)

# 获取token_type 两个点表示不是两个层级，表示的是子孙层级
token_type=jsonpath.jsonpath(a_json,expr='$..token_type')
print(token_type)

# 如果同名的key，指明父级目录
token_type=jsonpath.jsonpath(a_json,expr='$..token_info.token_type')
print(token_type)