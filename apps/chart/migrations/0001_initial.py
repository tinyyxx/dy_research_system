# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-31 10:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('template', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='图表', help_text='图表名称', max_length=20, verbose_name='图表名称')),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='template.TemplateModel', verbose_name='所属模板')),
            ],
        ),
    ]
