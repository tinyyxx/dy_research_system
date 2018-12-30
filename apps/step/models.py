from django.db import models
from users.models import UserProfile
from chart.models import ChartModel
from template.models import TemplateModel


class StepModel(models.Model):
    index_name = models.CharField(default="", max_length=20, verbose_name="指标名称", help_text="指标名称")
    formula = models.CharField(default="", max_length=200, help_text="计算公式")
    user = models.ForeignKey(UserProfile, verbose_name="用户ID", on_delete=models.CASCADE)
    # template = models.ForeignKey(TemplateModel, null=True, verbose_name="所属模板", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    frequency = models.IntegerField()


class StepData(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()
    type_name = models.CharField(max_length=30)
    value = models.CharField(max_length=20)
    # def __init__(self, **kwargs):
    #     for field in ('id', 'date', 'n/a', 'type_name', 'value', 'crate_at', 'update_at'):
    #         setattr(self, field, kwargs.get(field, None))


