from django.db import models
from category.models import CategoryModel
# Create your models here.


class IndexModel(models.Model):
    name = models.CharField(default="指标名称", max_length=20, verbose_name="指标名称", help_text="指标名称")
    category = models.ForeignKey(CategoryModel, null=False, blank=False, verbose_name="指标名称", help_text="指标",
                                 on_delete=models.CASCADE)
