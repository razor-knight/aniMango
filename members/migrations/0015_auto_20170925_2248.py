# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0014_auto_20170923_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]