# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 06:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PostEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ohoystudio_url', models.CharField(max_length=300)),
                ('ohoystudio_img_src_url', models.CharField(max_length=300)),
                ('youtube_url', models.TextField(default='')),
                ('call1', models.CharField(max_length=100)),
                ('call2', models.CharField(max_length=100)),
                ('naver_map_url', models.CharField(max_length=500)),
                ('kakao_link_label', models.TextField(max_length=500)),
                ('image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image4', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image5', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image6', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image7', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image8', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image9', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image10', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image12', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image13', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image14', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image15', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('image16', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=event.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
