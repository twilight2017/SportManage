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
    # 多对多关系用外键关联到学生类
    com_stu = models.ManyToManyField(to=Students, related_name="cho_com", null=True, blank=True,default=None)
    # 报名总人数
    com_total = models.CharField(max_length=50, default='0')
    # 有关成绩信息的文件
    com_mark = models.CharField(max_length=200, null=True, blank=True)
    com_infor= models.CharField(max_length=200, null=True, blank=True)