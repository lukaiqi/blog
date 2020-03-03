from django.db import models


# Create your models here.

class Client(models.Model):
    ip = models.CharField(max_length=20, default='', verbose_name='IP')
    addr = models.CharField(max_length=20, default='', verbose_name='地区')
    isp_name = models.CharField(max_length=20, default='', verbose_name='运营商')
    path = models.CharField(max_length=20, default='', verbose_name='访问路径')
    plantform = models.CharField(max_length=10, default='', verbose_name='操作系统')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='访问时间')

    class Meta:
        verbose_name = '访客IP'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip
