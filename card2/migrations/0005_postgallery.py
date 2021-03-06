# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 13:21
from __future__ import unicode_literals

import card2.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('card2', '0004_postnotcomment_kakao_thumbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gallery_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('gallery_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('gallery_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card2.PostNotComment')),
            ],
        ),
    ]
