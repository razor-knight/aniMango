# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20161014_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='subtitle',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
