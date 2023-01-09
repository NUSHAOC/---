from django.contrib import admin
from django.urls import path, include

# from UserServer import dispatcher
from UserServer import views
from django.conf.urls.static import serve,static
from queryFile.views import search_place,search_Node
import modifyFile.views as root


urlpatterns = [
    path('index/', views.index),
    path('user/', views.login),
    path('register/', views.register),
    path('admin/', views.loginA),
    path('', views.commencement),
    path('user/map/', search_place),
    path('admin/maproot/', include('modifyFile.urls')),
    path('user/map/search/', search_Node)
]
