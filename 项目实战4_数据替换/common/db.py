import pymysql


class DataBase:
    def __init__(self, host=None, port=3306, user=None, password=None, database=None):
        # 建立连接
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, database=database)

    def query_one(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        one = cursor.fetchone()
        cursor.close()
        return one

    def query_all(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        all_ = cursor.fetchall()
        cursor.close()
        return all_

    def close(self):
        self.close()


if __name__ == "__main__":
    from 项目实战5_注册接口.config.setting import Config

    db_config = Config.db
    db = DataBase(db_config['host'],
                  db_config['port'],
                  db_config['user'],
                  db_config['password'],
                  db_config['database'])

    sql = 'select id,mobile_code from yami_shops.tz_sms_log where user_phone="11223456784" order by id desc limit 5'
    result = db.query_one(sql)
    print(result)

# TODO
# tuple的数据换成字典
# 事务
# 使用字典拆包
# 注册：数据生成、数据替换
# 进一步优化