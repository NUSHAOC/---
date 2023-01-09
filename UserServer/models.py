# admin.site.register(Customer)
# 可以增加管理员使用的表
from django.contrib import admin
from django.db import models


class UserAccount(models.Model):
    UserId = models.CharField(max_length=32)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    PhoneNum = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    IsAdmin = models.CharField(max_length=50)


class UserAdmin(admin.ModelAdmin):
    list_display = ('UserId', 'UserName', 'Password', 'PhoneNum', 'Email', 'IsAdmin')


admin.site.register(UserAccount, UserAdmin)

'''
# 封装了对User数据的增删改查
# Dao=Database Access Object 数据库访问对象

class LogDao:
    # 创建数据库对象

    mySQL = MySQLUtil('account', 'userlog')  # 注意后续要加表名，库名

    # 执行数据库查询操作，返回查询结果
    @classmethod
    def query(cls, user):
        dataDict = {"username": user.username, "password": user.password}
        return cls.mySQL.query(dataDict)

    # 执行数据库查询操作，查询用户是否存在，返回查询结果
    @classmethod
    def exists(cls, username):
        dataDict = {"username": username}
        return cls.mySQL.exists(dataDict)

    # 执行数据插入操作，把用户信息添加进mysql
    @classmethod
    def insert(cls, user):
        dataDict = {"username": user.username, "password": user.password}
        if cls.mySQL.insert(dataDict):
            return 1
        else:
            return 0

    # 修改密码
    @classmethod
    def changePasswd(cls, user):
        dataDict = {'changeCol': 'password = %s' % user.password, 'caluse': 'username = %s' % user.username}
        if cls.mySQL.update(dataDict):
            return 1
        else:
            return 0

    # 注销用户
    @classmethod
    def deleteUser(cls, user):
        dataDict = {'username': user.username}
        if cls.mySQL.delete(dataDict):
            return 1
        else:
            return 0
'''
