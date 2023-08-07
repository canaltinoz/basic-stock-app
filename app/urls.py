from django.urls import path,include
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('upload', views.upload,name='upload'),
    path('list',views.list, name='list'),
    path('list/<id>',views.list_id, name='list_id'),
    path('update/<id>',views.update,name='update'),
    path('delete/<id>',views.delete,name='delete')
]
