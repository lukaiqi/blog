from datetime import datetime

from django.db import models


# Create your models here.

class Sensor(models.Model):
    temperature = models.CharField(max_length=10, default='', verbose_name='温度')
    humidity = models.CharField(max_length=10, default='', verbose_name='湿度')
    illumination = models.CharField(max_length=10, default='', verbose_name='光照')
    pressure = models.CharField(max_length=10, default='', verbose_name='气压')
    altitude = models.CharField(max_length=10, default='', verbose_name='海拔')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = '环境值'
        verbose_name_plural = verbose_name
