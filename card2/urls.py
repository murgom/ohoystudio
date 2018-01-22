from django.urls import path
from . import views

app_name = "card2"

urlpatterns = [
    path('list/', views.post_list, name="post_list"),
    path('wedding<int:pk>/', views.post_detail, name='post_detail'),
    path('gallery<int:pk>/', views.gallery_image, name='gallery_image'),
    path('gallery2/<int:pk>/', views.sms_image, name='sms_image'),
]
