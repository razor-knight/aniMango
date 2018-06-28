# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-25 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showings', '0008_auto_20170923_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='cooldown_period',
            field=models.IntegerField(blank=True, default=0, help_text=b'In days. Will be filled when saving according to type of show. Input the value manually to override.', null=True),
        ),
    ]