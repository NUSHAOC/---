from django.db.models.fields import json
from django.shortcuts import render
import modifyFile.models as nodb
from modifyFile.models import Neo4jutil, RedisUtil
from django import forms
from django.http import HttpResponse


class PlaceForm(forms.Form):
    Node = forms.CharField(label='Node', max_length=50)
    Id = forms.CharField(label='Id', max_length=50)
    Log = forms.CharField(label='Log', max_length=50)
    Lat = forms.CharField(label='Lat', max_length=50)
    linkNode1 = forms.CharField(label='lNode', max_length=200)
    linkNode2 = forms.CharField(label='lNode', max_length=200)
    # Type = forms.CharField(label='Type', max_length=200)


def Create_map(request):
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    if request.method == 'POST':
        place = request.POST
        # print(place)
        if place:
            name = place.get('Node')
            id = place.get('Id')
            log = place.get('Log')
            lat = place.get('Lat')
            adjacentNode = place.get('aNode')
            adjacentNode = adjacentNode.split('；')
            adjacentDis = place.get('aDis')
            adjacentDis = adjacentDis.split('；')
            node = {'name': name, 'id': id, 'log': log, 'lat': lat}
            redb.set(name, id)
            nedb.createNode(node)
            for i in range(0, (len(adjacentNode)-1)):
                nedb.createRelation(id, adjacentNode[i], adjacentDis[i])
            # return render(request, 'mapRoot.html', {'result': '成功添加地点！'})
            reb = "True"
            return render(request, 'mapRoot.html', {"result": reb})

    else:
        place = PlaceForm()
        red = "Flase"
        node = {'name': '', 'id': '', 'log': '', 'lat': '', 'result': red}
        return render(request, 'mapRoot.html', node)


def Delete_map(request):
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    if request.method == 'POST':
        place = request.POST
        # print(place)
        if place:
            name = place.get('Node')
            id = place.get('Id')
            log = place.get('Log')
            lat = place.get('Lat')
            node = {'name': name, 'id': id, 'log': log, 'lat': lat}
            redb.delete(name)
            nedb.deleteNode(node)
            reb = "True"
            return render(request, 'mapRoot.html', {"result": reb})
    else:
        place = PlaceForm()
        red = "Flase"
        node = {'name': '', 'id': '', 'log': '', 'lat': '', 'result': red}
        return render(request, 'mapRoot.html', node)


def Change_map(request):
    nedb = Neo4jutil(URL="http://localhost:11008",
                     USR="neo4j",
                     KEY="4468663578"
                     )
    redb = RedisUtil(host="127.0.0.1",
                     password="4468663578cxc",
                     db=0,
                     port=6379)
    if request.method == 'POST':
        place = request.POST
        # print(place)
        if place:
            name = place.get('Node')
            newname = place.get('newNode')
            # id = place.get('Id')
            log = place.get('Log')
            lat = place.get('Lat')
            id = redb.get(name)
            node = {'name': newname, 'id': id, 'log': log, 'lat': lat}
            redb.delete(name)
            redb.set(newname, id)
            nedb.changeNode(node)
            reb = "True"
            return render(request, 'mapRoot.html', {"result": reb})
    else:
        place = PlaceForm()
        red = "Flase"
        node = {'name': '', 'id': '', 'log': '', 'lat': '', 'result': red}
        return render(request, 'mapRoot.html', node)


def MapRoot(request):
    return render(request, 'mapRoot.html')
