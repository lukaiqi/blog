import datetime
import os
from time import strftime
from django.db import models


def filepath(instance, filename):
    ext = os.path.splitext(filename)[1]
    name = strftime('%Y%m%d%H%M%S')
    return os.path.join('music', name + ext)


class Music(models.Model):
    name = models.CharField(max_length=30, default='', verbose_name='名称')
    url = models.FileField(upload_to=filepath, verbose_name='文件路径')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '音乐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Sentence(models.Model):
    content = models.CharField(max_length=30, default='', verbose_name='名称')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '句子'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
