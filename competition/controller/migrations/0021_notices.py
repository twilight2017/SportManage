# Generated by Django 3.0.5 on 2020-06-01 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0020_competitions_com_infor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('not_name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]