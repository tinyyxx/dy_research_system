from django.db import models

# Create your models here.
from template.models import TemplateModel


class ChartModel(models.Model):
    title = models.CharField(default="图表", max_length=20, verbose_name="图表名称", help_text="图表名称")
    template = models.ForeignKey(TemplateModel, verbose_name="所属模板", on_delete=models.CASCADE)
