from django.urls import path
from . import views

# if you have more than one app and links get same name use 
# app_name and then give a name then in the link do this
# url "app_name:url"
# app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add')
]
