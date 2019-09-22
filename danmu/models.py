from datetime import datetime

from django.db import models


# Create your models here.
class Danmu(models.Model):
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    content = models.TextField(default='', verbose_name='弹幕')
    sendtime = models.DateTimeField(default=None, verbose_name='发送时间')

    class Meta:
        verbose_name = '弹幕'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Jinyan(models.Model):
    otype = models.CharField(max_length=10, default='1', verbose_name='操作者类型')
    snic = models.CharField(max_length=50, default='', verbose_name='操作者昵称')
    dnic = models.CharField(max_length=50, default='', verbose_name='被禁言昵称')
    endtime = models.CharField(max_length=20, default='', verbose_name='禁言结束时间')

    class Meta:
        verbose_name = '禁言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dnic


class Liwu(models.Model):
    nickname = models.CharField(max_length=50, default='', verbose_name='昵称')
    gfid = models.CharField(max_length=10, default='', verbose_name='礼物id')
    gfcnt = models.CharField(max_length=10, default='1', verbose_name='礼物数量')
    hits = models.CharField(max_length=10, default='1', verbose_name='连击数')

    class Meta:
        verbose_name = '礼物'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
