import json
from django.http import JsonResponse


# def dispatch(request):
#     if request.method == 'GET':
#         request.params = request.GET
#
#     elif request.method in ['POST', 'PUT', 'DELETE']:
#         request.params = json.loads(request.body)
#
#     action = request.params['action']
#     if action == '':
#         return
#     elif action == '':
#         return
#     elif action == '':
#         return
#     elif action == '':
#         return
#
#     else:
#         return JsonResponse({'ret': 1, 'msg': '不支持该类型的http请求'})
