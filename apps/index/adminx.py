#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import IndexModel


class IndexModelAdmin(object):
    list_display = ["name", ]


xadmin.site.register(IndexModel, IndexModelAdmin)
