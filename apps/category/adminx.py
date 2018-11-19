#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import CategoryModel


class CategoryModelAdmin(object):
    list_display = ["name", "parent_category", "is_index"]


xadmin.site.register(CategoryModel, CategoryModelAdmin)
