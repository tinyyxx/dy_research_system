# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-11-02 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartmodel',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='所属用户'),
            preserve_default=False,
        ),
    ]
