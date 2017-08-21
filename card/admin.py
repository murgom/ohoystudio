from django.contrib import admin
from card.models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'author', 'title','post_content_str','image1','created_at', 'updated_at']

    def post_content_str(self, post):
        return '동영상 링크 : {}'.format(str(post.youtube_url))


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','message','password','post_title_str','comment_content_len']

    def post_title_str(self,comment):
        return '{} 게시물 글'.format(str(comment.post.title))

    def comment_content_len(self,comment):
        return '댓글 : {}글자'.format(len(comment.message))

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        return qs.select_related('post')
