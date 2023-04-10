"""
json结构 --> json schema
1、某个字段是否存在
2、某个字段长度、类型、空
3、列表当中的数据


-----
required ：['access_token','token_type']
'access_token':{"type":"string","length":34}
-----


"""
import jsonschema

response={'access_token':'b2c4f19c-b2c4f19c-bb4d-4f81-936d-9d6ff9b22266',
          'token_type':'bearer',
          'refresh_token':'3e91671e-a34b-4ab5-baf3-13e401229e24',
          'expires_in':1259599,
          'msg':'ok'}

# 断言有没有access_token
schema={"required":['access_token',"msg","token_type"]}
# 校验某个字段值是否存在
resp=jsonschema.validate(response,schema=schema)
print(resp)

# # 属性个数
# schema = {
#     "required":['access_token',"msg","token_type"],
#     "minProperties":1,
#     "MaxProperties":3
# }
# resp=jsonschema.validate(response,schema=schema)
# print(resp)

# 判断指定的字段的类型
schema = {
    "required":['access_token',"msg","token_type"],
    "properties":{
        "access_token":{"type":"string"},
        "token_type":{"type":"string"},
        "msg":{"type":"string"}
    }
}
resp=jsonschema.validate(response,schema=schema)
print(resp)

# 校验指定属性（字符串）长度是多少
schema = {
    "required":['access_token',"msg","token_type"],
    "properties":{

        "token_type":{"type":"string","maxLength":7,"pattern":"bearer"}
    }
}
resp=jsonschema.validate(response,schema=schema)
print(resp)