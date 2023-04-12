"""Tudosok URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import handler404
from .views import *

urlpatterns = [

    path('admin/', admin.site.urls),
    path('',index_view,name='index'),
    path('Neumann',Neumann_view,name="Neumann"),
    path('Puskas_Tivadar',Puskas_view,name="Puskas"),
    path('Jedlik_Anyos',Jedlik_view,name='Jedlik'),
    path('Rubik_Erno',Rubik_view,name='Rubik'),
    path('Question1',Question1_view,name='quiz'),
    path('Question2',Question2_view),
    path('Question3',Question3_view),
    path('Question4',Question4_view),
    path('Question5',Question5_view),
    path("Result",Result_view)

    
]
