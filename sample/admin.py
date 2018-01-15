from django.contrib import admin
from sample.models import SampleImage, SampleGalleryImage, SampleSmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(SampleImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '(sample)청첩장 이름 : {}'.format(str(post.title))

@admin.register(SampleGalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'post_content_str','gallery_image1','created_at', 'updated_at']
    list_display_links = ('post_content_str',)

    def post_content_str(self, post):
        return '연결된 청첩장(샘플) : {}'.format(str(post.post))

@admin.register(SampleSmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']
