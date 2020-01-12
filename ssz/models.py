from datetime import datetime

from django.db import models


# Create your models here.
class Bilibili(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='标题')
    play = models.CharField(max_length=8, default='', verbose_name='播放量')
    likes = models.CharField(max_length=8, default='', verbose_name='点赞数')
    reply = models.CharField(max_length=8, default='', verbose_name='评论数')
    danmaku = models.CharField(max_length=8, default='', verbose_name='弹幕数')
    favorite = models.CharField(max_length=8, default='', verbose_name='收藏数')
    coin = models.CharField(max_length=8, default='', verbose_name='硬币数')
    share = models.CharField(max_length=8, default='', verbose_name='分享数')
    pubtime = models.CharField(max_length=15, default='', verbose_name='发布时间')
    querydate = models.CharField(max_length=15, default='', verbose_name='查询日期')

    class Meta:
        verbose_name = '哔哩哔哩'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class QQMusic(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='标题')
    comments = models.CharField(max_length=10, default='', verbose_name='评论数')
    pubdate = models.CharField(max_length=15, default='', verbose_name='发布时间')
    querydate = models.CharField(max_length=15, default='', verbose_name='查询日期')

    class Meta:
        verbose_name = 'QQ音乐'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
