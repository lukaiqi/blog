from datetime import datetime

from django.db import models


# Create your models here.
class Homepic(models.Model):
    url = models.ImageField(upload_to='homepic', verbose_name='图片地址')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='上传时间')

    class Meta:
        verbose_name = '首页图片'
        verbose_name_plural = verbose_name

        def __str__(self):
            return self.url
