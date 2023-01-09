import py2neo as py2neo
from django.db import models
from py2neo import *
import redis

from redis import Redis, ConnectionPool


class RedisUtil:
    # redis连接

    def __init__(self, host, password, db, port):
        self.con = Redis(host=host, port=port, password=password, db=db)

    # 判断键是否存在
    def exists(self, key):
        return self.con.exists(key)

    # 获取键值
    def get(self, key):
        res = self.con.get(key).decode("utf-8")
        return res

    # 存储键值
    def set(self, key, value):
        # 键值存储在缓存中，保留时间为120秒
        self.con.set(key, value)

    # 删除键值
    def delete(self, key):
        self.con.delete(key)

    # 连接池
    # 当程序创建数据源实例时，系统会一次性创建多个数据库连接，并把这些数据库连接保存在连接池中
    # 当程序需要进行数据库访问时，无需重新新建数据库连接，而是从连接池中取出一个空闲的数据库连接


class Neo4jutil:

    def __init__(self, URL, USR, KEY):
        link = Graph(URL, auth=(USR, KEY))
        self.graph = link

    #  查询地点
    def queryNode(self, nodeId):
        sql = "match (n:Place) where Id(n) = " + nodeId + " return n"
        answer = self.graph.run(sql).data()
        return answer

    # 查询最短路径 （Dijkstra算法）
    def matchBestPath(self, start, end):
        sql = "MATCH (s:Place {Id:'" + start + "'}),(e:Place{Id:'" + end + "'}),p=shortestPath((s)-[*..100]->(e)) " \
                                                                           "RETURN p "
        answer = self.graph.run(sql).data()
        return answer

    # 关系查询 整个地图（可以不需要）
    def allMap(self):
        answer = self.graph.run("MATCH (n1:Place)- [rel] -> (n2:Place) RETURN n1,rel,n2 ").data()
        return answer

    def findRelationByEntity1(self, entity1):
        answer = self.graph.run("MATCH (n1:Place {Id:\"" + entity1 + "\"})- [rel] -> (n2) RETURN n1,rel,n2").data()
        return answer

    # 关系查询：实体2
    def findRelationByEntity2(self, entity1):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2:Place {Id:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
        if len(answer) == 0:
            answer = self.graph.run(
                "MATCH (n1)- [rel] -> (n2:Place {Id:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
            if len(answer) == 0:
                answer = self.graph.run(
                    "MATCH (n1)- [rel] -> (n2:Place {Id:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
        return answer

    # # 创建节点
    # def createNode(self, node):
    #     sql = "create(n:" + str(node['type']) + \
    #           "{name: '" + str(node['name']) + "', long:" + float(node['long']) + \
    #           ",lat:" + float(node['lat']) + "}) return n"
    #     answer = self.graph.run(sql).data()
    #     return answer
    #
    # # 删除节点
    # def deleteNode(self, node):
    #     sql = "match (n:" + str(node['type']) + ") where n.name='" + str(node['name']) + \
    #           "' delete n"
    #     answer = self.graph.run(sql).data()
    #     return answer
    #
    # # 修改节点经纬度，修改类型建筑或道路需要删除重新建立
    # def changeNode(self, node):
    #     sql = "match (n:" + str(node['type']) + " { name: '" + str(node['name']) + "'}) set n.name='" \
    #           + node['newname'] + "', n.long=" + float(node['long']) + ", n.lat=" + float(node['lat'])
    #     answer = self.graph.run(sql).data()
    #     return answer


if __name__ == '__main__':
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    # test = nedb.queryNode(str(int(redb.get('霖雨桥')) - 1))
    # # print(test)
    # a = test[0]
    # a = a['n']
    # name = a['Name']
    # num = a['NUM']
    # lat = a['Lat']
    # log = a['Log']
    # describe = "没有简介写入，请联系我们补充~"
    # node = {'name': name, 'num': num, 'lat': lat, 'log': log, 'describe': describe}
    # print(node)
    print(nedb.)