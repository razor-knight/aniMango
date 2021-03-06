# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-09 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0018_auto_20180220_2058'),
        ('polls', '0002_auto_20180808_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.CharField(help_text=b'Episodes watched (Ep.1, Eps. 1-3), etc.', max_length=200, null=True)),
                ('lib_series', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='library.Series')),
                ('memberOf', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
        migrations.RemoveField(
            model_name='options',
            name='lib_series',
        ),
        migrations.DeleteModel(
            name='Options',
        ),
    ]
