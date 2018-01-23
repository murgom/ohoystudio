from django.urls import path
from . import views

app_name = "carousel_card"

urlpatterns = [
    path('list/', views.post_list, name="post_list"),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('gallery<int:pk>/', views.gallery_image, name='gallery_image'),
    path('gallery2/<int:pk>/', views.sms_image, name='sms_image'),

    path('sample<int:pk>/', views.sample_post_detail, name='sample_post_detail'),
    path('sample/gallery<int:pk>/', views.sample_gallery_image, name='sample_gallery_image'),
    path('sample/gallery2/<int:pk>/', views.sample_sms_image, name='sample_sms_image'),
]
