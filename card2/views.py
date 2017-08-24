from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card2.models import PostEvent
from .forms import PostNotCommentForm

def post_list(request):
    qs = PostEvent.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(PostEvent, pk=pk)

    return render(request, 'card3/post_detail.html', {
                                    'post': post,
                                    })
