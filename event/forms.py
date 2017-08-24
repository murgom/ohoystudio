from django import forms
from django.forms import ModelForm
from .models import PostEvent
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostEventForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    youtube_url = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = PostEvent
        fields = ('title','youtube_url',)
