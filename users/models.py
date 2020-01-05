from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    """
    用户信息
    性别：0男1女
    """
    # 用户注册，所以昵称，邮箱可以为空
    nickname = models.CharField(max_length=30, null=True, blank=True, verbose_name='昵称')
    gender = models.IntegerField(default=0, verbose_name='性别')
    email = models.EmailField(max_length=50, null=True, blank=True, verbose_name='邮箱')
    openid = models.CharField(max_length=50, null=True, blank=True, verbose_name='身份id')

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
