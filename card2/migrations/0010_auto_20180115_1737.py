# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-15 08:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card2', '0009_infomationimage_preview_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='galleryimage',
            options={'verbose_name': '갤러리', 'verbose_name_plural': '갤러리'},
        ),
        migrations.AlterModelOptions(
            name='infomationimage',
            options={'verbose_name': '댓글없는 청첩장', 'verbose_name_plural': '댓글없는 청첩장(메인)'},
        ),
        migrations.AlterModelOptions(
            name='smsimage',
            options={'verbose_name': '2G 핸드폰공유 이미지', 'verbose_name_plural': '2G 핸드폰공유 이미지'},
        ),
        migrations.RemoveField(
            model_name='infomationimage',
            name='massage_image15',
        ),
    ]
