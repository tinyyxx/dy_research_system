from django.db import models
from users.models import UserProfile
from chart.models import ChartModel
# Create your models here.


class StepModel(models.Model):
    index_name = models.CharField(default="", max_length=20, verbose_name="指标名称", help_text="指标名称")
    user = models.ForeignKey(UserProfile, verbose_name="用户ID", on_delete=models.CASCADE)
