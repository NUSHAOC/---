import py2neo as py2neo
from django.db import models
from py2neo import Graph
import redis

from redis import Redis, ConnectionPool


class Neo4jutil:

    def __init__(self, URL, USR, KEY):
        link = Graph(URL, auth=(USR, KEY))
        self.graph = link

    def createNode(self, node):
        sql = "create(n:Place " + \
              "{Id:'" + node['id'] + "',Name: '" + node['name'] + "', Log:" + node['log'] + \
              ",Lat:" + node['lat'] + "})"
        answer = self.graph.run(sql).data()
        return answer

    # 删除节点
    def deleteNode(self, node):
        sql = "match (n:Place) where n.Id='" + node['id'] + "'detach delete n"
        answer = self.graph.run(sql).data()
        return answer

    # 修改节点经纬度，修改类型（建筑或道路）需要删除重新建立
    def changeNode(self, node):
        sql = "match (n:Place{Id: '" + node['id'] + "'}) set n.Name='" \
              + node['name'] + "', n.Log=" + node['log'] + ", n.Lat=" + node['lat']
        answer = self.graph.run(sql).data()
        return answer

    def createRelation(self, id, name, dis):
        sql = "match (n:Place{Id:'" + id + "'}),(s:Place{Name:'" + name + "'}) " \
            "create (n)-[p:Distance{distance:" + dis + "}]->(s) return p"
        answer = self.graph.run(sql).data()
        return answer

    def queryNode(self, node):
        sql = "match (n:Place { Id: '" + node['id'] + "'}) return n"
        answer = self.graph.run(sql).data()
        return answer

    # 查询最短路径 待修改A*
    # def matchBestPath(self, start, end):
    #     sql = "MATCH (start:" + str(start['type']) + "{name:'" + str(start['name']) + "'}),(end:" + str(end['type']) + \
    #           " {name:'" + str(end['name']) + "'}) " \
    #   "CALL apoc.algo.dijkstra(start, end, 'weight_property',1.0) YIELD path, weight return weight"
    #     answer = self.graph.run(sql).evaluate()
    #     return answer
    #
    # def findRelationByEntity1(self, entity1):
    #     answer = self.graph.run("MATCH (n1:person {name:\"" + entity1 + "\"})- [rel] -> (n2) RETURN n1,rel,n2").data()
    #     return answer

    # 关系查询：起始地点+关系
    def findOtherEntities(self, entity, relation):
        answer = self.graph.run(
            "MATCH (n1:person {name:\"" + entity + "\"})-[rel:" + relation + "]->(n2) RETURN n1,rel,n2").data()
        return answer

    # 关系查询 整个图数据库
    def zhishitupu(self):
        answer = self.graph.run("MATCH (n1:person)- [rel] -> (n2) RETURN n1,rel,n2 ").data()
        return answer

    # 关系查询 目的地
    def findRelationByEntity2(self, entity1):
        answer = self.graph.run("MATCH (n1)- [rel] -> (n2:major {name:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
        if len(answer) == 0:
            answer = self.graph.run(
                "MATCH (n1)- [rel] -> (n2:level {name:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
            if len(answer) == 0:
                answer = self.graph.run(
                    "MATCH (n1)- [rel] -> (n2:univer {name:\"" + entity1 + "\"}) RETURN n1,rel,n2").data()
        return answer

    # 创建节点


class RedisUtil:
    # redis连接

    def __init__(self, host, password, db, port):
        self.con = Redis(host=host, port=port, password=password,db=db)

    def exists(self, key):
        return self.con.exists(key)

    # 存储键值,

    def set(self, key, value):
        # 键值存储在缓存中，保留时间为120秒
        self.con.set(key, value)

    # 获取键值

    def get(self, key):
        res = self.con.get(key).decode("utf-8")
        return res

    # 删除键值

    def delete(self, key):
        self.con.delete(key)


if __name__=='__main__':
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
