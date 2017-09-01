from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card2.models import PostNotComment, PostGallery, PostGallery2
from .forms import PostNotCommentForm

def post_list(request):
    qs = PostNotComment.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(PostNotComment, pk=pk)

    return render(request, 'card2/post_detail.html', {
                                    'post': post,
                                    })

def post_gallery(request, pk):
    post = get_object_or_404(PostGallery, pk=pk)

    return render(request, 'card2/post_gallery.html', {
                                    'post': post,
                                    })

def post_gallery2(request, pk):
    post = get_object_or_404(PostGallery2, pk=pk)

    return render(request, 'card2/post_gallery2.html', {
                                    'post': post,
                                    })
