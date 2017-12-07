from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name="post_list"),
    url(r'^wedding(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^gallery_card(?P<pk>\d+)/$', views.post_gallery, name='post_gallery'),
    url(r'^gallery_card2/(?P<pk>\d+)/$', views.sms_image, name='sms_image'),
    url(r'^comments/$', views.comment_list, name='comment_list'),

    url(r'^comment/(?P<pk>\d+)/delete/$', views.comment_delete, name='comment_delete'),

    url(r'^preview/(?P<pk>\d+)/$', views.preview_image, name='preview_image'),
]
