from django.contrib import admin
from carousel_card.models import CarouselImage, CarouselGalleryImage, CarouselSmsImage,SampleCarouselImage,SampleCarouselGalleryImage,SampleCarouselSmsImage
from django_summernote.admin import SummernoteModelAdmin

@admin.register(CarouselImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '청첩장 이름(이미지 회전) : {}'.format(str(post.title))


@admin.register(CarouselGalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','post_content_str','created_at', 'updated_at']
    list_display_links = ('name',)

    def post_content_str(self, post):
        return '연결된 청첩장(이미지 회전) : {}'.format(str(post.post))

@admin.register(CarouselSmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']


@admin.register(SampleCarouselImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'title','post_content_str','created_at', 'updated_at']
    list_display_links = ('title',)

    def post_content_str(self, post):
        return '(샘플)청첩장 이름(이미지 회전) : {}'.format(str(post.title))

@admin.register(SampleCarouselGalleryImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','post_content_str','created_at', 'updated_at']
    list_display_links = ('name',)

    def post_content_str(self, post):
        return '(샘플)연결된 청첩장(이미지 회전) : {}'.format(str(post.post))

@admin.register(SampleCarouselSmsImage)
class PostNotCommentAdmin(SummernoteModelAdmin):
    list_display = ['id', 'name','message_image1','created_at', 'updated_at']