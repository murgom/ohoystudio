# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card2', '0005_postgallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postnotcomment',
            name='ohoystudio_img_src_url',
        ),
    ]
