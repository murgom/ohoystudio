from django.contrib import admin
from card2.models import InfomationImage, GalleryImage, SmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(InfomationImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '청첩장 이름 : {}'.format(str(post.title))

@admin.register(GalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','gallery_image1','created_at', 'updated_at']

@admin.register(SmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']
