# json 表示
import json

a_json = '{"name":"ice"}'
a_json = "{\"name\":\"ice\"}"

a_json = '{"name":"ice","age":19,"male":false,"hobby":[],"a":{},"args":null}'

# json数据
b_json = '[1,2,3]'

# json 转成  字典（列表）
# 反序列化
a_dict=json.loads(a_json)
print(a_dict)




# 字典（列表）  转成  json
# 序列化
b_dict={"a":"hello"}
b_json=json.dumps(b_dict)
print(b_dict)