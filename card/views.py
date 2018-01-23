from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card.models import Post, PostGallery ,Comment, SmsImage, SamplePost,SamplePostGallery ,SampleComment, SampleSmsImage
from .forms import PostForm, CommentForm, CommentDeleteForm, SamplePostForm, SampleCommentForm, SampleCommentDeleteForm
from django.views.generic import DeleteView

from django.contrib import messages

def post_list(request):
    qs = Post.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render(request, 'card/post_detail.html', {
                                    'post': post,
                                    'form': form,
                                    })

def post_gallery(request, pk):
    post = get_object_or_404(PostGallery, pk=pk)

    return render(request, 'card/post_gallery.html', {
                                    'post': post,
                                    })

def sms_image(request, pk):
    post = get_object_or_404(SmsImage, pk=pk)

    return render(request, 'card/sms_image.html', {
                                    'post': post,
                                    })


def comment_list(request):
    qs = Comment.objects.all().order_by('-id').select_related('post')

    return render(request, 'card/post_detail.html',{
        'comment_list':qs,
    })


def comment_delete(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
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
    return render(request, 'card/comment_delete.html', {
                                    'form': form,
                                    })

def sample_post_detail(request, pk):
    post = get_object_or_404(SamplePost, pk=pk)
    form = SampleCommentForm(request.POST or None)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.path)
    return render(request, 'card/sample_post_detail.html', {
                                    'post': post,
                                    'form': form,
                                    })

def sample_post_gallery(request, pk):
    post = get_object_or_404(SamplePostGallery, pk=pk)

    return render(request, 'card/sample_post_gallery.html', {
                                    'post': post,
                                    })

def sample_sms_image(request, pk):
    post = get_object_or_404(SampleSmsImage, pk=pk)

    return render(request, 'card/sample_sms_image.html', {
                                    'post': post,
                                    })


def sample_comment_list(request):
    qs = SampleComment.objects.all().order_by('-id').select_related('post')

    return render(request, 'card/sample_post_detail.html',{
        'comment_list':qs,
    })


def sample_comment_delete(request, pk):
    comment = get_object_or_404(SampleComment, pk=pk)
    if request.method == "POST":
        form = SampleCommentDeleteForm(request.POST, instance=comment)
        if form.is_valid():
            comment.password1 == comment.password2
            comment.delete()
            messages.success(request, '삭제했습니다.')
        else:
            messages.warning(request, '패스워드가 다릅니다')
    else:
        form = SampleCommentDeleteForm(instance=comment)
    return render(request, 'card/sample_comment_delete.html', {
                                    'form': form,
                                    })