# Generated by Django 2.1.7 on 2019-12-15 14:20

import datetime
from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.FileField(upload_to=photos.models.filepath, verbose_name='图片地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '照片',
                'verbose_name_plural': '照片',
            },
        ),
    ]
