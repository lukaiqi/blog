# Generated by Django 2.1.7 on 2019-09-22 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jinghua', '0003_auto_20190922_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jinghua',
            name='otime',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='操作时间'),
        ),
    ]