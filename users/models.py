from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    Gender_Choice = (
                     ('male', '男'),
                     ('female', '女')
                     )
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default=" ")
    birthday = models.DateField(verbose_name="生日", null=True, blank=True)
    gender = models.CharField(max_length=5, choices=Gender_Choice, verbose_name="昵称", default="female")
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    # 没有上传文件切换为image/default
    image = models.ImageField(upload_to="image/%Y/%m", default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
