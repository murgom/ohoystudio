from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from event.models import PostEvent
from .forms import PostEvent

def post_list(request):
    qs = PostEvent.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(PostEvent, pk=pk)

    return render(request, 'event/post_detail.html', {
                                    'post': post,
                                    })
