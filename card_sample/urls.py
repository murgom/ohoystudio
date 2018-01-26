from django.urls import path
from . import views

app_name = "card_sample"

urlpatterns = [
    path('list/', views.post_list, name="post_list"),
    path('wedding<int:pk>/', views.post_detail, name='post_detail'),
    path('gallery_card<int:pk>/', views.post_gallery, name='post_gallery'),
    path('gallery_card2/<int:pk>/', views.sms_image, name='sms_image'),
    path('comments/', views.comment_list, name='comment_list'),

    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
]