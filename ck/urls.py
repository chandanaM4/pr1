"""
URL configuration for ck project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main, name='main'),
    path('at/', at, name='at'),
    path('add/', adding, name='adding'),
    path('um/', um, name='um'),
    path('up/', update, name='update'),
    path('fr/', fr, name='fr'),
    path('find/', find, name='find'),
    path('d/', d, name='d'),
    path('delete/', delete, name='delete'), 
    path('viewstudent/', viewstudent, name='viewstudent')
]
