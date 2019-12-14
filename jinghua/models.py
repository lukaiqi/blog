from django.db import models
from datetime import datetime


# Create your models here.
class Jinghua(models.Model):
    nickname = models.CharField(max_length=30, default='', verbose_name='昵称')
    otime = models.DateTimeField(default=datetime.now, verbose_name='操作时间')
    status = models.CharField(max_length=2, default='1', verbose_name='状态')

    class Meta:
        verbose_name = '词条净化'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
