from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card3.models import PostNotComment
from .forms import PostNotCommentForm

def post_list(request):
    qs = PostNotComment.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(PostNotComment, pk=pk)

    return render(request, 'card2/post_detail.html', {
                                    'post': post,
                                    })
