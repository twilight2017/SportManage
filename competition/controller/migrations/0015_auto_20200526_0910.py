# Generated by Django 3.0.5 on 2020-05-26 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0014_auto_20200526_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='com_stu',
            field=models.ManyToManyField(to='controller.Students'),
        ),
    ]