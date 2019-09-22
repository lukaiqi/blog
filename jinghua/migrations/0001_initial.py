# Generated by Django 2.1.7 on 2019-09-22 16:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jinghua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=30, verbose_name='昵称')),
                ('otime', models.DateTimeField(default=datetime.datetime(2019, 9, 22, 16, 56, 53, 412030), verbose_name='操作时间')),
                ('status', models.CharField(default='1', max_length=2, verbose_name='状态')),
            ],
        ),
    ]
