from django.contrib import admin
from card2.models import InfomationImage, GalleryImage, SmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(InfomationImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'author', 'title','post_content_str','main_image1','created_at', 'updated_at']

    def post_content_str(self, post):
        return '동영상 링크 : {}'.format(str(post.youtube_url))

@admin.register(GalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','gallery_image1','created_at', 'updated_at']

@admin.register(SmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']
