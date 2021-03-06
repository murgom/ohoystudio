from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from card2.models import InfomationImage, GalleryImage, SmsImage, SampleInfomationImage,SampleGalleryImage, SampleSmsImage
from .forms import PostNotCommentForm, SamplePostNotCommentForm

def post_list(request):
    qs = InfomationImage.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(InfomationImage, pk=pk)

    return render(request, 'card2/post_detail.html', {
                                    'post': post,
                                    })

def gallery_image(request, pk):
    post = get_object_or_404(GalleryImage, pk=pk)

    return render(request, 'card2/gallery_image.html', {
                                    'post': post,
                                    })

def sms_image(request, pk):
    post = get_object_or_404(SmsImage, pk=pk)

    return render(request, 'card2/sms_image.html', {
                                    'post': post,
                                    })




def sample_post_detail(request, pk):
    post = get_object_or_404(SampleInfomationImage, pk=pk)

    return render(request, 'card2/sample_post_detail.html', {
                                    'post': post,
                                    })

def sample_gallery_image(request, pk):
    post = get_object_or_404(SampleGalleryImage, pk=pk)

    return render(request, 'card2/sample_gallery_image.html', {
                                    'post': post,
                                    })

def sample_sms_image(request, pk):
    post = get_object_or_404(SampleSmsImage, pk=pk)

    return render(request, 'card2/sample_sms_image.html', {
                                    'post': post,
                                    })