# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='samplegalleryimage',
            options={'verbose_name': '갤러리(샘플)', 'verbose_name_plural': '갤러리(샘플)'},
        ),
        migrations.AlterModelOptions(
            name='sampleimage',
            options={'verbose_name': '샘플 청첩장', 'verbose_name_plural': '샘플 청첩장(메인)'},
        ),
        migrations.AlterModelOptions(
            name='samplesmsimage',
            options={'verbose_name': '2G 핸드폰공유 이미지(샘플)', 'verbose_name_plural': '2G 핸드폰공유 이미지(샘플)'},
        ),
        migrations.RemoveField(
            model_name='sampleimage',
            name='massage_image15',
        ),
    ]
