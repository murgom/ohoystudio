from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from sample.models import SampleImage, SampleGalleryImage, SampleSmsImage

def post_list(request):
    qs = SampleImage.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(SampleImage, pk=pk)

    return render(request, 'sample/post_detail.html', {
                                    'post': post,
                                    })

def gallery_image(request, pk):
    post = get_object_or_404(SampleGalleryImage, pk=pk)

    return render(request, 'sample/gallery_image.html', {
                                    'post': post,
                                    })

def sms_image(request, pk):
    post = get_object_or_404(SampleSmsImage, pk=pk)

    return render(request, 'sample/sms_image.html', {
                                    'post': post,
                                    })
