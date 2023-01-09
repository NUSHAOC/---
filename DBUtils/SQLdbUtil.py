import pymysql


class MySQLUtil:

    # 连接数据库,并生成全局可用的连接对象和查询游标
    def __init__(self, dbName, tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.con = pymysql.connect(
            host='localhost',
            user='root',
            password="4468663578cxc()",
            database=self.dbName,
            port=3306,
        )
        self.cursor = self.con.cursor()

    # 关闭全局游标，断开全局连接
    def disconnect(self):
        self.cursor.close()
        self.con.close()

    # 查询用户名是否存在
    def exists(self, dataDict):
        caluse = ''
        for key, value in dataDict.items():
            caluse += key + '="' + value + '"'
        # print(caluse)
        sql = """select * from %s where  %s ;""" % (self.tableName, caluse)
        return self.execute(sql)

    # 验证用户名和密码是否正确
    def query(self, dataDict):
        # 查询子条件拼接
        caluse = ''
        for key, value in dataDict.items():
            caluse += key + '="' + value + '" and '
        caluse = caluse[:-4]
        # print(caluse)
        sql = """select * from %s where %s;""" % (self.tableName, caluse)

        return self.execute(sql)

    # 添加新用户
    def insert(self, dataDict):
        # sql语句拼接
        columns = ''
        values = ''
        for key, value in dataDict.items():
            columns += key + ','
            values += '"' + value + '",'
        columns = columns[:-1]
        values = values[:-1]
        sql = """insert into %s (%s) VALUES (%s);""" % (self.tableName, columns, values)
        # print(sql)
        return self.execute(sql)

    # 更新
    def update(self, dataDict):
        # sql语句拼接
        changeCol = dataDict['changeCol']  # 要改变值的列名
        caluse = dataDict['caluse']  # 要改变值的子条件
        sql = 'update %s set %s where %s' % (self.tableName, changeCol, caluse)
        return self.execute(sql)

    # 删除
    def delete(self, dataDict):
        # sql语句拼接
        caluse = ''
        for key, value in dataDict.items():
            caluse += key + '="' + value + '"'

        sql = """delete from %s where %s;""" % (self.tableName, caluse)
        # print(sql)
        return self.execute(sql)

    # print(sql)

    # 执行sql语句
    def execute(self, sql):
        self.connect()
        affected = 0
        try:
            affected = self.cursor.execute(sql)
        except BaseException as e:
            print(e)
            affected = 0
        finally:
            self.con.commit()
            self.disconnect()
            return affected

