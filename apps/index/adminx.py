#!/usr/bin/env python
# encoding: utf-8
import xadmin
from .models import IndexModel


class IndexModelAdmin(object):
    list_display = ["name", "category"]

    def get_media(self):
        media = super(IndexModelAdmin, self).get_media()
        path = self.request.get_full_path()
        if "add" in path or 'update' in path:
            media.add_js([self.static('xadmin/js/xadmin.js')])
        return media


xadmin.site.register(IndexModel, IndexModelAdmin)
