from django.db import models


# B站投稿视频
class Videolist(models.Model):
    aid = models.CharField(max_length=15, default='', verbose_name='视频id', primary_key=True)
    title = models.CharField(max_length=100, default='', verbose_name='标题')
    play = models.CharField(max_length=8, default='', verbose_name='播放量')
    like_count = models.CharField(max_length=8, default='', verbose_name='点赞数')
    reply = models.CharField(max_length=8, default='', verbose_name='评论数')
    danmaku = models.CharField(max_length=8, default='', verbose_name='弹幕数')
    favorite = models.CharField(max_length=8, default='', verbose_name='收藏数')
    coin = models.CharField(max_length=8, default='', verbose_name='硬币数')
    share = models.CharField(max_length=8, default='', verbose_name='分享数')
    pubtime = models.CharField(max_length=20, default='', verbose_name='发布时间')
    add_time = models.CharField(max_length=20, default='', verbose_name='查询日期')

    class Meta:
        verbose_name = '视频列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


# B站统计信息
class UserInfo(models.Model):
    follows = models.CharField(max_length=10, default='', verbose_name='关注数')
    fans = models.CharField(max_length=10, default='', verbose_name='粉丝数')
    likes = models.CharField(max_length=10, default='', verbose_name='总点赞数')
    plays = models.CharField(max_length=10, default='', verbose_name='总播放量')
    add_time = models.CharField(max_length=20, default='', verbose_name='记录日期')

    class Meta:
        verbose_name = '基础信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.fans
