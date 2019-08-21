from datetime import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class ArticleType(models.Model):
    name = models.CharField(max_length=10, verbose_name='分类名字')

    class Meta:
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    type_name = models.ForeignKey(ArticleType, on_delete=models.CASCADE, verbose_name='文章分类')
    click_num = models.IntegerField(default=0, verbose_name='点击数')
    content = RichTextUploadingField()
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
