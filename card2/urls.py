from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name="post_list"),
    url(r'^wedding(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^gallery(?P<pk>\d+)/$', views.post_gallery, name='post_gallery'),
]
