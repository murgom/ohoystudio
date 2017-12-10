# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 02:32
from __future__ import unicode_literals

import card2.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('card2', '0008_auto_20170908_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='infomationimage',
            name='preview_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path),
        ),
    ]