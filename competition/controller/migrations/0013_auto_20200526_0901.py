# Generated by Django 3.0.5 on 2020-05-26 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0012_competitions_com_stu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitions',
            name='com_stu',
            field=models.ManyToManyField(default='None', to='controller.Students'),
        ),
    ]