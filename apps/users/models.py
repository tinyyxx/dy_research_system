from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    last_login_ip_frontend = models.CharField(max_length=50, verbose_name=u"前端上次登录IP", null=True, blank=True)
    last_login_ip_backend = models.CharField(max_length=50, verbose_name=u"后端上次登录IP", null=True, blank=True)

    gender = models.CharField(max_length=6, choices=(("male", u"男"), ("female", u"女")), null=True, blank=True)
    mobile_phone = models.CharField(max_length=11, null=True, blank=True)

    class Meta:
        verbose_name = "用户管理"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username

