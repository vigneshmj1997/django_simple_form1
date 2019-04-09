from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('upload', views.publish,name="upload"),
    path('view', views.see,name="see"),
    path('delete', views.delete_,name="del"),
    
]