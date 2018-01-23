from django import forms
from django.forms import ModelForm
from .models import InfomationImage, SampleInfomationImage
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostNotCommentForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    youtube_url = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = InfomationImage
        fields = ('title','youtube_url',)


class SamplePostNotCommentForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    youtube_url = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = SampleInfomationImage
        fields = ('title','youtube_url',)