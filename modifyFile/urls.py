from django.contrib import admin
from django.urls import path, include

# from UserServer import dispatcher
from UserServer import views
from django.conf.urls.static import serve,static
from queryFile.views import search_place
import modifyFile.views as root


urlpatterns = [
    path('', root.MapRoot),
    path('create/', root.Create_map),
    path('delete/', root.Delete_map),
    path('change/', root.Change_map),
]
