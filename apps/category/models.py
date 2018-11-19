from django.db import models

# Create your models here.


class CategoryModel(models.Model):
    """
    左侧导航栏目录
    """
    # CATEGORY_TYPE = (
    #     (1, "一级类目"),
    #     (2, "二级类目"),
    #     (3, "三级类目"),
    # )
    IS_INDEX = (
        (0, "否"),
        (1, "是")
    )
    name = models.CharField(default="目录名称", max_length=20, verbose_name="目录名称", help_text="目录名称")

    # category_type = models.IntegerField(verbose_name="目录级别", help_text="目录级别")  # choices=CATEGORY_TYPE,

    parent_category = models.ForeignKey("self", null=True, blank=True,  verbose_name="所属父目录", help_text="父目录",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_index = models.IntegerField(choices=IS_INDEX, default=0, verbose_name="是否是指标")

    class Meta:
        verbose_name = "目录管理"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
