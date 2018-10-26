# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-22 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181019_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='last_login_ip',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login_ip_backend',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='后端上次登录IP'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_login_ip_frontend',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='前端上次登录IP'),
        ),
    ]