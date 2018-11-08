#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import CategoryModel


class CategoryModelAdmin(object):
    list_display = ["name", "category_type", "parent_category"]


xadmin.site.register(CategoryModel, CategoryModelAdmin)
