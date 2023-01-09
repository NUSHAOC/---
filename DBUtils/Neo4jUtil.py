from py2neo import *


class Neo4jutil:
    URL = "http://localhost:7474"
    USR = "neo4j"
    KEY = "4468663578"

    def __init__(self, uri):
        link = Graph(url=self.URL, auth=(self.USR, self.KEY))
        self.graph = link

    # 创建节点
    def createNode(self, node):
        sql = "create(n:" + str(node['type']) + \
              "{name: '" + str(node['name']) + "', long:" + float(node['long']) +\
              ",lat:" + float(node['lat']) + "}) return n"
        answer = self.graph.run(sql).data()
        return answer

    # 删除节点
    def deleteNode(self, node):
        sql = "match (n:" + str(node['type']) + ") where n.name='" + str(node['name']) + \
              "' delete n"
        answer = self.graph.run(sql).data()
        return answer

    # 修改节点经纬度，修改类型建筑或道路需要删除重新建立
    def changeNode(self, node):
        sql = "match (n:" + str(node['type']) + " { name: '" + str(node['name']) + "'}) set n.name='"\
              + node['newname'] + "', n.long=" + float(node['long']) + ", n.lat=" + float(node['lat'])
        answer = self.graph.run(sql).data()
        return answer

    def queryNode(self, node):
        sql = "match (n:" + str(node['type']) + " { name: '" + str(node['name']) + "'}) return n"
        answer = self.graph.run(sql).data()
        return answer

    # 查询最短路径 待修改A*
    def matchBestPath(self, start, end):
        sql = "MATCH (start:" + str(start['type']) + "{name:'" + str(start['name']) + "'}),(end:" + str(end['type']) + \
              " {name:'" + str(end['name']) + "'}) " \
              "CALL apoc.algo.dijkstra(start, end, 'weight_property',1.0) YIELD path, weight return weight"
        answer = self.graph.run(sql).evaluate()
        return answer
