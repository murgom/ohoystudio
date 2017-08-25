from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    youtube_url = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = Post
        fields = ('title','youtube_url',)



class CommentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = Comment
        fields = ('author','user','password','message',)

    def clean_verify_password(self):
        password1 = self.cleaned_data.get('password',None)
        if password1 != password1:
            raise forms.ValidationError('암호가 틀렸습니다')
        return password1
