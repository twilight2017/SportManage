from django.db import models

# models用于和数据库交互，Django提供ORM，无须自行编写sql语句
# Create your models here.


class Students(models.Model):

    stu_id = models.CharField(max_length=50, default='None')
    stu_name = models.CharField(max_length=50, default='None')
    stu_gender = models.CharField(max_length=10, default='None')
    identity = models.CharField(max_length=50, default='None')
    stu_college = models.CharField(max_length=50, default='None')
    stu_mail = models.CharField(max_length=50, default='None')
    stu_password = models.CharField(max_length=50, default='None')
    # 供于展示对象的函数

    def to_dict(self):
        return{
            'stu_id': self.stu_id,
            'stu_name': self.stu_name,
            'stu_gender': self.stu_gender,
            'identity': self.identity,
            'stu_college': self.stu_college,
            'stu_mail': self.stu_mail,
        }


class Admins(models.Model):
    adm_id = models.CharField(max_length=50, default='None')
    adm_name = models.CharField(max_length=50, default='None')
    adm_gender = models.CharField(max_length=50, default='None')
    identity = models.CharField(max_length=50, default='None')
    adm_college = models.CharField(max_length=50, default='None')
    adm_mail = models.CharField(max_length=50, default='None')
    adm_password = models.CharField(max_length=50, default='None')


# 比赛模型类

class Competitions(models.Model):
    com_id = models.CharField(max_length=50, default='None')
    com_name = models.CharField(max_length=50, default='None')
    com_startime = models.CharField(max_length=50, default='2018/10/10')
    com_endtime = models.CharField(max_length=50, default='None')
    com_type = models.CharField(max_length=50, default='None')
    com_college = models.CharField(max_length=50, default='None')
    # 报名总人数
    com_total = models.CharField(max_length=50, default='0')