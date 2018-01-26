# Generated by Django 2.0.1 on 2018-01-23 03:17

import card2.models
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('card2', '0012_sampleinfomationimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleGalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gallery_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('gallery_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('gallery_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card2.InfomationImage')),
            ],
            options={
                'verbose_name': '갤러리',
                'verbose_name_plural': '갤러리',
            },
        ),
        migrations.CreateModel(
            name='SampleSmsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('message_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('message_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card2.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card2.InfomationImage')),
            ],
            options={
                'verbose_name': '2G 핸드폰공유 이미지',
                'verbose_name_plural': '2G 핸드폰공유 이미지',
            },
        ),
        migrations.AlterModelOptions(
            name='sampleinfomationimage',
            options={'verbose_name': '(샘플)댓글없는 청첩장', 'verbose_name_plural': '(샘플)댓글없는 청첩장(메인)'},
        ),
    ]