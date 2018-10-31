from django.db import models

# Create your models here.
from users.models import UserProfile
from chart.models import ChartModel


class TemplateModel(models.Model):
    """
    用户自定义模板
    """
    title = models.CharField(default="我的模板",  max_length=20, verbose_name="自定义模板名称", help_text="自定义模板名称")
    user = models.ForeignKey(UserProfile, verbose_name="用户ID", on_delete=models.CASCADE)
    chart = models.ForeignKey(ChartModel, verbose_name="图表ID", on_delete=models.CASCADE)
