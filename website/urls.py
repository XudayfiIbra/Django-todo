from django.urls import path
from . import views
urlpatterns = [
    path('', views.test, name="test"),
    path('<str:name>', views.test, name="test"),
]
