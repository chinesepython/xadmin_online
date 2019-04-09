from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    Gender_Choice = (
                     ('male', '男'),
                     ('female', '女')
                     )
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default=" ")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=6, choices=Gender_Choice, verbose_name="昵称", default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 没有上传文件切换为image/default
    image = models.ImageField(upload_to="image/%Y/%m", default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 邮箱验证码
class EmailVerifyRecord(models.Model):
    SEND_TYPE_STATUS = (("register", "注册"),
                        ("forget", "找回密码"))
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=SEND_TYPE_STATUS, default='register', max_length=19, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        # 复数形式和verbose_name保持一致，不然后台显示会自动显示为“邮箱验证码s”
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


# 轮播图
class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', verbose_name='轮播图', max_length=100)
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name



