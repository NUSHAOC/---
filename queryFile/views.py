from django import forms
from django.db.models.fields import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from queryFile.models import Neo4jutil, RedisUtil
import queryFile.models as nodb


class PlaceForm(forms.Form):
    Start = forms.CharField(label='起始地点', max_length=50)
    End = forms.CharField(label='目的地点', max_length=50)
    AnyPlace = forms.CharField(label='查询地点', max_length=50)
    Distance = forms.CharField(label='距离', max_length=50)


#   等待表单路由实现可细化拆分，取消不必要的判断
def search_place(request):
    ctx = {}
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    if request.method == 'POST':
        # getPlaceFrom = PlaceForm(request.GET)
        Start = request.GET['Start']
        End = request.GET['End']
        AnyPlace = request.GET['AnyPlace']
        searchResult = {}
        # if Start == '' and End == '' and AnyPlace == '':
        #     searchResult = nodb.allMap(nedb)
        #     return render(request, 'index.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})

        if Start == '' and End == '' and AnyPlace != '':
            if redb.exists(AnyPlace):
                placeId = redb.get(AnyPlace)
                searchResult = nedb.queryNode(placeId)
                return render(request, 'index.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                return render(request, 'index.html', {'Error': '该地点未收录！'})

        if Start != '' and End != '':
            if redb.exists(Start) and redb.exists(End):
                startId = str(int(redb.get(Start)) - 1)
                endId = str(int(redb.get(End)) - 1)
                searchResult = nedb.matchBestPath(startId, endId)
                return render(request, 'index.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
            else:
                if redb.exists(Start) == '' and redb.exists(End) == '':
                    return render(request, 'index.html', {'Error': '起始地点和目的地点都未收录！'})
                elif redb.exists(Start):
                    return render(request, 'index.html', {'Error': '目的地点未收录！'})
                elif redb.exists(End):
                    return render(request, 'index.html', {'Error': '起始地点未收录！'})
    else:
        return render(request, 'index.html')
        # 若只输入地点1,则输出与地点1有直接关系的地点和关系
        # if len(entity1) != 0 and len(relation) == 0 and len(entity2) == 0:
        #     searchResult = nedb.findRelationByEntity1(entity1)
        #     return render(request, 'map.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        #
        # # 若只输入地点2则,则输出与地点2有直接关系的地点和关系
        # if len(entity2) != 0 and len(relation) == 0 and len(entity1) == 0:
        #     searchResult = nedb.findRelationByEntity2(entity2)
        #     if len(searchResult) > 0:
        #         return render(request, 'map.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        #
        # # 若输入地点和距离，则输出与地点具有距离x的关系的其他地点
        # if len(entity1) != 0 and len(relation) != 0 and len(entity2) == 0:
        #     searchResult = nedb.findOtherEntities(entity1, relation)
        #     # searchResult = sortDict(searchResult)
        #     if len(searchResult) > 0:
        #         return render(request, 'map.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})
        #
        # # 若输入目的地和距离，则输出与目的地具有距离x关系的其他地点
        # if len(entity2) != 0 and len(relation) != 0 and len(entity1) == 0:
        #     searchResult = nedb.findOtherEntities2(entity2, relation)
        #     # searchResult = sortDict(searchResult)
        #     if len(searchResult) > 0:
        #         return render(request, 'map.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})

        # # 全为空 则输出整个地图
        # if len(entity1) == 0 and len(relation) == 0 and len(entity2) == 0:
        #     searchResult = nedb.zhishitupu()
        #     # searchResult = sortDict(searchResult)
        # # print(json.loads(json.dumps(searchResult)))
        # return render(request, 'map.html', {'searchResult': json.dumps(searchResult, ensure_ascii=False)})


def search_Node(request):
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    state = 200
    if request.method == 'GET':
        nodeName = request.GET['spot_name']
        if nodeName != '':
            if redb.exists(nodeName):
                searchResult = nedb.queryNode(str(int(redb.get(nodeName)) - 1))
                searchResult = searchResult[0]
                searchResult = searchResult['n']
                name = searchResult['Name']
                num = searchResult['NUM']
                lat = searchResult['Lat']
                log = searchResult['Log']
                describe = "没有简介写入，请联系我们补充~"
                res = {"name": name, "num": num, "lat": lat, "log": log, "describe": describe}
                return JsonResponse({"state":state,"info":res})
            else:
                statue = 404
                return JsonResponse({"state":statue})
        else:
            statue = 404
            return JsonResponse({"state":statue})
