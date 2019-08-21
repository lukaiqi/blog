from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models
from article.models import Article

User = get_user_model()


# Create your models here.
class Comment(models.Model):
    pid = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='文章id')
    content = models.TextField(default='', verbose_name='评论内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content
