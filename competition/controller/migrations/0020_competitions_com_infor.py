# Generated by Django 3.0.5 on 2020-05-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0019_auto_20200528_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='competitions',
            name='com_infor',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]