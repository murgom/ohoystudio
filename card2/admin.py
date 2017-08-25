from django.contrib import admin
from card2.models import PostNotComment, PostGallery
from django_summernote.admin import SummernoteModelAdmin

@admin.register(PostNotComment)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'author', 'title','post_content_str','main_image1','created_at', 'updated_at']

    def post_content_str(self, post):
        return '동영상 링크 : {}'.format(str(post.youtube_url))

@admin.register(PostGallery)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','gallery_image1','created_at', 'updated_at']
