from django.contrib import admin
from card.models import Post, PostGallery ,Comment, SmsImage, SamplePost, SamplePostGallery ,SampleComment, SampleSmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','main_image1','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '청첩장 이름(댓글O) : {}'.format(str(post.title))


@admin.register(PostGallery)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','post_content_str','created_at', 'updated_at']
    list_display_links = ('name',)

    def post_content_str(self, post):
        return '연결된 청첩장(댓글O) : {}'.format(str(post.post))

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title_str','post_user_str','post_message_str','password1','comment_content_len']
    list_display_links = ('post_user_str','post_title_str')
    # prepopulated_fields = { 'password2': ['password1'] }

    def post_user_str(self,comment):
        return '작성자 : {}'.format(str(comment.user))

    def post_message_str(self,comment):
        return '댓글 내용 : {}'.format(str(comment.message))

    def post_title_str(self,comment):
        return '{} 게시물 댓글'.format(str(comment.post.title))

    def comment_content_len(self,comment):
        return '댓글 : {}글자'.format(len(comment.message))

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        return qs.select_related('post')

@admin.register(SmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']


@admin.register(SamplePost)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','main_image1','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '(샘플)청첩장 이름(댓글O) : {}'.format(str(post.title))

@admin.register(SamplePostGallery)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','post_content_str','created_at', 'updated_at']
    list_display_links = ('name',)

    def post_content_str(self, post):
        return '(샘플)연결된 청첩장(댓글O) : {}'.format(str(post.post))

@admin.register(SampleComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title_str','post_user_str','post_message_str','password1','comment_content_len']
    list_display_links = ('post_user_str','post_title_str')
    # prepopulated_fields = { 'password2': ['password1'] }

    def post_user_str(self,comment):
        return '(샘플)작성자 : {}'.format(str(comment.user))

    def post_message_str(self,comment):
        return '(샘플)댓글 내용 : {}'.format(str(comment.message))

    def post_title_str(self,comment):
        return '(샘플){} 게시물 댓글'.format(str(comment.post.title))

    def comment_content_len(self,comment):
        return '(샘플)댓글 : {}글자'.format(len(comment.message))

    def get_queryset(self,request):
        qs = super().get_queryset(request)
        return qs.select_related('post')

@admin.register(SampleSmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']