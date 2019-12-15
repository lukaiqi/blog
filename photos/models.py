import datetime
import os
import uuid
from django.db import models


def filepath(instance, filename):
    ext = os.path.splitext(filename)[1]
    name = str(uuid.uuid4())
    return os.path.join('photo', name + ext)


class Photo(models.Model):
    url = models.FileField(upload_to=filepath, verbose_name='图片地址')
    add_time = models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '照片'
        verbose_name_plural = verbose_name
