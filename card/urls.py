from django.urls import path
from . import views

app_name = "card"

urlpatterns = [
    path('list/', views.post_list, name="post_list"),
    path('wedding<int:pk>/', views.post_detail, name='post_detail'),
    path('gallery_card<int:pk>/', views.post_gallery, name='post_gallery'),
    path('gallery_card2/<int:pk>/', views.sms_image, name='sms_image'),
    path('comments/', views.comment_list, name='comment_list'),

    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),


    # path('sample/wedding<int:pk>/', views.sample_post_detail, name='sample_post_detail'),
    # path('sample/gallery_card<int:pk>/', views.sample_post_gallery, name='sample_post_gallery'),
    # path('sample/gallery_card2/<int:pk>/', views.sample_sms_image, name='sample_sms_image'),
    # path('sample/comments/', views.sample_comment_list, name='sample_comment_list'),
    
    # path('sample/comment/<int:pk>/delete/', views.sample_comment_delete, name='sample_comment_delete'),
]