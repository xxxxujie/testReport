"""
jsonpath:指的是获取json指定字段的路径
"""

a_json = {
    "msg":"ok",
    "data":{
        "token_info":{
            "token":"abc",
            "token_type":"bearer"
        }
    },
    "id":123,
    "name":"yuze"
}

a_json["data"]["token_info"]["token_type"]