# Generated by Django 3.0.5 on 2020-05-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm_id', models.CharField(default='None', max_length=50)),
                ('adm_name', models.CharField(default='None', max_length=50)),
                ('adm_gender', models.BooleanField(default='None', max_length=50)),
                ('adm_college', models.CharField(default='None', max_length=50)),
                ('adm_mail', models.CharField(default='None', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(default='None', max_length=50)),
                ('stu_name', models.CharField(default='None', max_length=50)),
                ('stu_gender', models.BooleanField(default=False)),
                ('stu_grade', models.CharField(default='None', max_length=50)),
                ('stu_class', models.CharField(default='None', max_length=50)),
                ('stu_college', models.CharField(default='None', max_length=50)),
                ('stu_mail', models.CharField(default='None', max_length=50)),
            ],
        ),
    ]