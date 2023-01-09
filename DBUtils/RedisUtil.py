import redis


# class RedisUtil:
#     # redis连接
#     def __init__(self,
#                  host,
#                  port,
#                  password,
#                  db):
#         self.host = host
#         self.port = port
#         self.password = password
#         self.db = db
#         self.con = None
#         self.lock = False
#
#     def connect(self):
#         self.con = redis.Redis(self.host,
#                                self.port,
#                                self.password,
#                                self.db,
#                                decode_responses=True  # 默认bytes解码成字符串
#                                )
#         self.con.ping()
#         self.lock = True
#
#     # 连接池
#     # 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中
#     # 当程序需要进行数据库访问时，无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接
#
#     # 判断键是否存在
#     @classmethod
#     def exists(cls, key):
#         return cls.client.exists(key)
#
#     # 存储键值,
#     @classmethod
#     def set(cls, key, value):
#         # 键值存储在缓存中，保留时间为30秒
#         cls.client.setex(key, value, 30)
#
#     # 获取键值
#     @classmethod
#     def get(cls, key):
#         res = cls.client.get(key).decode("utf-8")
#         return res
#
#     # 删除键值
#     @classmethod
#     def delete(cls, key):
#         cls.client.delete(key)
