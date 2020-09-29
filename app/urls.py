from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('',views.index,name="index"),
    path('save/',views.save,name="save"),
    path('show/',views.show,name="show"),
]
