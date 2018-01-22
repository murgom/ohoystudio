# Generated by Django 2.0.1 on 2018-01-22 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_remove_postevent_ohoystudio_img_src_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postevent',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
