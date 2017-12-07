# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-07 02:11
from __future__ import unicode_literals

import card.models
from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0021_previewimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='previewimage',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='preview_image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card.models.get_image_path),
        ),
        migrations.DeleteModel(
            name='PreviewImage',
        ),
    ]