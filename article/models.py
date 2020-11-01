from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

from utils.generate_id import IdWorker

User = get_user_model()


class ArticleType(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名字')

    class Meta:
        verbose_name = '类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.CharField(max_length=30, primary_key=True, verbose_name='id')
    title = models.CharField(max_length=50, default='', verbose_name='标题')
    type = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章分类')
    desc = models.TextField(default='', verbose_name='概述')
    content = RichTextUploadingField()
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = IdWorker(1, 2, 0).get_id()
        super().save(**kwargs)

    class Meta:
        verbose_name = '列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id', related_name='comments')
    content = models.TextField(default='', verbose_name='评论内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='评论用户')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='添加时间')

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
