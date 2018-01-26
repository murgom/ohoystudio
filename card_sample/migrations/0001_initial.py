# Generated by Django 2.0.1 on 2018-01-26 08:33

import card_sample.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=200)),
                ('password1', models.CharField(max_length=50)),
                ('password2', models.CharField(blank=True, max_length=50)),
                ('message', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '(샘플)댓글',
                'verbose_name_plural': '(샘플)댓글',
            },
        ),
        migrations.CreateModel(
            name='SamplePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('ohoystudio_url', models.CharField(max_length=300)),
                ('youtube_url', models.TextField(default='')),
                ('call1', models.CharField(max_length=100)),
                ('call2', models.CharField(max_length=100)),
                ('naver_map_url', models.CharField(max_length=500)),
                ('kakao_link_label', models.TextField(max_length=500)),
                ('main_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('invitation_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('family_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('call1_image4', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('call2_image5', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('celendar_image6', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('gallery_image7', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('videotitle_image8', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('map_image9', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('map_infor_image10', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('message_title_image11', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('kakao_image12', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('story_image13', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('facebook_image14', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('copyright_image16', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('kakao_thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('preview_image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '(샘플)댓글있는 청첩장',
                'verbose_name_plural': '(샘플)댓글있는 청첩장(메인)',
            },
        ),
        migrations.CreateModel(
            name='SamplePostGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gallery_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('gallery_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('gallery_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card_sample.SamplePost')),
            ],
            options={
                'verbose_name': '(샘플)갤러리',
                'verbose_name_plural': '(샘플)갤러리',
            },
        ),
        migrations.CreateModel(
            name='SampleSmsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message_image1', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('message_image2', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('message_image3', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=card_sample.models.get_image_path)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card_sample.SamplePost')),
            ],
            options={
                'verbose_name': '(샘플)2G 핸드폰공유 이미지',
                'verbose_name_plural': '(샘플)2G 핸드폰공유 이미지',
            },
        ),
        migrations.AddField(
            model_name='samplecomment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='card_sample.SamplePost'),
        ),
    ]
