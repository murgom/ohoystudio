from django.contrib import admin
from card2.models import InfomationImage, GalleryImage, SmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(InfomationImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '청첩장 이름(댓글X) : {}'.format(str(post.title))

@admin.register(GalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','post_content_str','created_at', 'updated_at']
    list_display_links = ('name',)

    def post_content_str(self, post):
        return '연결된 청첩장(댓글X) : {}'.format(str(post.post))
        
@admin.register(SmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']
