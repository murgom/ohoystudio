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


class PostNotComment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    ohoystudio_url = models.CharField(max_length=300)
    ohoystudio_img_src_url = models.CharField(max_length=300)
    youtube_url = models.TextField(default='')
    call1 = models.CharField(max_length=100)
    call2 = models.CharField(max_length=100)
    naver_map_url = models.CharField(max_length=500)
    kakao_link_label = models.TextField(max_length=500)
    image1 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image2 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image3 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image4 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image5 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image6 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image7 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image8 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image9 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image10 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image12 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image13 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image14 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image15 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    image16 = ProcessedImageField(blank=True,
            processors=[Thumbnail(1920, 1080)],
            upload_to=get_image_path,
            format='JPEG',
            )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('card:post_detail',args=[self.id])
