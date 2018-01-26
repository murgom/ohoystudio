from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card_sample.models import SamplePost, SamplePostGallery ,SampleComment, SampleSmsImage
from .forms import PostForm, CommentForm, CommentDeleteForm
from django.views.generic import DeleteView

from django.contrib import messages

def post_list(request):
    qs = SamplePost.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(SamplePost, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render(request, 'card_sample/post_detail.html', {
                                    'post': post,
                                    'form': form,
                                    })

def post_gallery(request, pk):
    post = get_object_or_404(SamplePostGallery, pk=pk)

    return render(request, 'card_sample/post_gallery.html', {
                                    'post': post,
                                    })

def sms_image(request, pk):
    post = get_object_or_404(SampleSmsImage, pk=pk)

    return render(request, 'card_sample/sms_image.html', {
                                    'post': post,
                                    })


def comment_list(request):
    qs = SampleComment.objects.all().order_by('-id').select_related('post')

    return render(request, 'card_sample/post_detail.html',{
        'comment_list':qs,
    })


def comment_delete(request, pk):
    comment = get_object_or_404(SampleComment, pk=pk)
    if request.method == "POST":
        form = CommentDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            comment.password1 == comment.password2
            comment.delete()
            messages.success(request, '삭제했습니다.')
        else:
            messages.warning(request, '패스워드가 다릅니다')
    else:
        form = CommentDeleteForm(instance=comment)
    return render(request, 'card_sample/comment_delete.html', {
                                    'form': form,
                                    })