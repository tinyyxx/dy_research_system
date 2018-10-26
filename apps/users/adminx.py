#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liyao
@license: Apache Licence 
@contact: yli@posbao.net
@site: http://www.piowind.com/
@software: PyCharm
@file: adminx.py
@time: 2017/7/4 17:04
"""
import xadmin
from xadmin import views
from users.models import UserProfile


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "研究系统"
    site_footer = "Deya Research System"
    # menu_style = "accordion"


class UserProfileAdmin(object):
    list_display = ['id', 'username', 'is_superuser', 'is_active', 'email', 'mobile_phone',
                    'date_joined', 'last_login_ip_frontend', 'last_login_ip_backend']

# class VerifyCodeAdmin(object):
#     list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
#xadmin.site.register(UserProfile, UserProfileAdmin)
