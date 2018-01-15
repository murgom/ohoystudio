# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 05:10
from __future__ import unicode_literals

import carousel_card.models
from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('carousel_card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image10',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image4',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image5',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image6',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image7',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image8',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='gallery_image9',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to=carousel_card.models.get_image_path),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image10_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image10_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image1_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image1_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image2_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image2_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image3_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image3_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image4_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image4_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image5_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image5_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image6_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image6_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image7_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image7_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image8_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image8_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image9_explain',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='carouselgalleryimage',
            name='image9_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='carouselgalleryimage',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
