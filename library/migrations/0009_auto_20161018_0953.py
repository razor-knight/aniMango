# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_auto_20160930_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='ani_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='cover_link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='synopsis',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='title',
            field=models.CharField(blank=True, max_length=110),
        ),
        migrations.AlterField(
            model_name='series',
            name='title_eng',
            field=models.CharField(blank=True, max_length=110),
        ),
    ]
