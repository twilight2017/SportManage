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
from django.views.static import serve
from competition.settings import FILES_ROOT

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
    path('admpeople/', views.admpeople, name='ADMPEOPLE'),
    path('admgroup/<str:man_name>', views.admgroup, name='ADMGROUP'),
    path('admmark/', views.admmark, name='ADMARK'),
    # 用于管理员上传比赛成绩文件
    path('admmark/<str:ma_name>', views.upload, name="UPLOAD"),
    path('mark/', views.mark, name="MARK"),
    path('mark/<str:file_name>', views.download, name="DOWNLOAD"),
    # 用于管理员上传赛程信息文件
    path('admpeople/<str:infor_name>', views.groupup, name="GROUPUP"),
    # 用于生成赛程信息
    path('ADMGROUP/<str:export_name>', views.create_info, name="EXPORT"),
    # 用于发布公告
    path('admhome/<int:distinct_n>', views.upnotice, name="UPNOTICE"),
    path('attention/', views.attention, name="ATTENTION")
]
