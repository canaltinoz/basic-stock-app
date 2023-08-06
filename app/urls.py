from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('upload', views.upload,name='upload'),
    path('list',views.list, name='list'),
    path('get',views.get,name='get')
]
