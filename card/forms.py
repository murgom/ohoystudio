from django import forms
from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from django.utils.translation import ugettext, ugettext_lazy as _


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=100)
    youtube_url = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'src':'img-responsive img-rounded'} ))

    class Meta:
        model = Post
        fields = ('title','youtube_url',)



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author','user','password1','message',)


class CommentDeleteForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Comment
        fields = ('author','user','password1','message',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2