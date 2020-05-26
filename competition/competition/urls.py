"""competition URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path
from controller import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name="REGISTER"),
    path('', views.login, name="LOGIN"),
    path('home/', views.home, name="HOME"),
    path('admhome/', views.admhome, name="ADMHOME"),
    path('logout/', views.logout),
    path('private/', views.private, name="PRIVATE"),
    path('admprivate/', views.admprivate, name="ADMPRIVATE"),
    path('admadd/', views.create_com, name="ADMADD"),
    path('admdeliver/', views.admdeliver, name="ADMDELIVER"),
    path('choice/', views.deliver, name="CHOICE"),
    path('admdeliver/<str:del_name>', views.delete, name="DELETE"),
    path('choice/<str:join_name>', views.join, name='JOIN'),
    path('consult/', views.consult, name='CONSULT'),


]
