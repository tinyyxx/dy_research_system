from django.db import models

# Create your models here.
from users.models import UserProfile


class TemplateModel(models.Model):
    """
    用户自定义模板
"""
    title = models.CharField(default="自定义模板",  max_length=30, verbose_name="自定义模板", help_text="自定义模板")
    user = models.ForeignKey(UserProfile, verbose_name="用户ID", on_delete=models.CASCADE)

