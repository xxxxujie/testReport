"""
1.准备数据库的信息，url、端口、名称
2.python怎么操作数据库，pymysql、dataset、pip install pymysql
3.建立连接
4.游标
5.执行sql语句
6.得到结果

游标：建议每次执行sql时都重新初始化一个新的游标，
"""
import pymysql

# 建立连接
conn = pymysql.connect(host='47.113.180.81',
                       port=3306,
                       user='lemon',
                       password='lemon123')

# 建立游标
cursor = conn.cursor()

# 执行sql语句
sql = 'select id,mobile_code from yami_shops.tz_sms_log where user_phone="11223456784" order by id desc limit 5'
result = cursor.execute(sql)
print(result)

# 获取查询结果
one = cursor.fetchone()
print(one)

all_ = cursor.fetchall()
print(all_)

# 不管是游标，还是连接，用完了关掉
cursor.close()
conn.close()