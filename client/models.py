from django.db import models


# Create your models here.

class Client(models.Model):
    ip = models.CharField(max_length=20, default='', verbose_name='IP')
    country = models.CharField(max_length=20, default='', verbose_name='国家')
    city = models.CharField(max_length=20, default='', verbose_name='城市')
    area = models.CharField(max_length=20, default='', verbose_name='地区')
    isp = models.CharField(max_length=20, default='', verbose_name='运营商')
    path = models.TextField(default='', verbose_name='访问路径')
    user_agent = models.TextField(default='', verbose_name='请求头')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='访问时间')

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ip
