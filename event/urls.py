from django.conf.urls import url
from django.urls import path
from . import views

app_name = "event"

urlpatterns = [
    path('list/', views.post_list, name="post_list"),
]
