# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 20:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0006_auto_20170920_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='last_reply_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 20, 20, 29, 19, 511275, tzinfo=utc)),
            preserve_default=False,
        ),
    ]