# Generated by Django 2.1.7 on 2019-08-23 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Danmu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(default='', max_length=50, verbose_name='昵称')),
                ('content', models.TextField(default='', verbose_name='弹幕')),
                ('sendtime', models.CharField(default='', max_length=20, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '弹幕',
                'verbose_name_plural': '弹幕',
            },
        ),
    ]
