# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-20 06:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0006_auto_20170820_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='naver_map_url',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
