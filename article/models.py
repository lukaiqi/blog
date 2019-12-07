from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

User = get_user_model()


class ArticleType(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名字')

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    type_name = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章分类')
    desc = models.TextField(default='', verbose_name='概述')
    content = RichTextUploadingField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    pid = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id')
    content = models.TextField(default='', verbose_name='评论内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
