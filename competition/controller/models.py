from django.db import models

# models用于和数据库交互，Django提供ORM，无须自行编写sql语句
# Create your models here.

class Students(models.Model):
    stu_id = models.CharField(max_length=50, default='None')
    stu_name = models.CharField(max_length=50, default='None')
    stu_gender = models.BooleanField(default=False)
    stu_grade = models.CharField(max_length=50,default='None')
    stu_class = models.CharField(max_length=50,default='None')
    stu_college = models.CharField(max_length=50,default='None')
    stu_mail = models.CharField(max_length=50,default='None')

class Admins(models.Model):
    adm_id = models.CharField(max_length=50,default='None')
    adm_name = models.CharField(max_length=50,default='None')
    adm_gender = models.BooleanField(max_length=50,default='None')
    adm_college = models.CharField(max_length=50,default='None')
    adm_mail = models.CharField(max_length=50,default='None')

