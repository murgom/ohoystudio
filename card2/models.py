from django.conf import settings
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.contrib.auth.models import User

import uuid
import os

def get_image_path(instance, filename):
    return os.path.join('card2', "image2_%s" % str(instance), filename)


class InfomationImage(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    ohoystudio_url = models.CharField(max_length=300)
    youtube_url = models.TextField(default='')
    call1 = models.CharField(max_length=100)
    call2 = models.CharField(max_length=100)
    naver_map_url = models.CharField(max_length=500)
    kakao_link_label = models.TextField(max_length=500)
    main_image1 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    invitation_image2 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    family_image3 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    call1_image4 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    call2_image5 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    celendar_image6 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    gallery_image7 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    videotitle_image8 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    map_image9 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    map_infor_image10 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    kakao_image12 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    story_image13 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    facebook_image14 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    copyright_image16 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    kakao_thumbnail = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    preview_image = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '댓글없는 청첩장'
        verbose_name_plural = '댓글없는 청첩장(메인)'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('card2:post_detail',args=[self.id])

class GalleryImage(models.Model):
    post = models.ForeignKey(InfomationImage)
    name = models.CharField(max_length=100)
    gallery_image1 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    gallery_image2 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    gallery_image3 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '갤러리'
        verbose_name_plural = '갤러리'

class SmsImage(models.Model):
    post = models.ForeignKey(InfomationImage)
    name = models.CharField(max_length=100)
    message_image1 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    message_image2 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    message_image3 = ProcessedImageField(blank=True,
            processors=[Thumbnail(2000, 2000)],
            upload_to=get_image_path,
            format='JPEG',
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '2G 핸드폰공유 이미지'
        verbose_name_plural = '2G 핸드폰공유 이미지'