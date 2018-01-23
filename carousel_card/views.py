from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from carousel_card.models import CarouselImage, CarouselGalleryImage, CarouselSmsImage,SampleCarouselImage,SampleCarouselGalleryImage,SampleCarouselSmsImage

def post_list(request):
    qs = CarouselImage.objects.all().order_by('-id')

def post_detail(request, pk):
    post = get_object_or_404(CarouselImage, pk=pk)
    posts = get_object_or_404(CarouselGalleryImage, pk=pk)

    return render(request, 'carousel_card/post_detail.html', {
                                    'post': post,
                                    'posts':posts,
                                    })


def gallery_image(request, pk):
    posts = get_object_or_404(CarouselGalleryImage, pk=pk)

    return render(request, 'carousel_card/gallery_image.html', {
                                    'posts': posts,
                                    })

def sms_image(request, pk):
    post = get_object_or_404(CarouselSmsImage, pk=pk)

    return render(request, 'carousel_card/sms_image.html', {
                                    'post': post,
                                    })

def sample_post_detail(request, pk):
    post = get_object_or_404(SampleCarouselImage, pk=pk)
    posts = get_object_or_404(SampleCarouselGalleryImage, pk=pk)

    return render(request, 'carousel_card/sample_post_detail.html', {
                                    'post': post,
                                    'posts':posts,
                                    })

def sample_gallery_image(request, pk):
    posts = get_object_or_404(SampleCarouselGalleryImage, pk=pk)

    return render(request, 'carousel_card/sample_gallery_image.html', {
                                    'posts': posts,
                                    })

def sample_sms_image(request, pk):
    post = get_object_or_404(SampleCarouselSmsImage, pk=pk)

    return render(request, 'carousel_card/sample_sms_image.html', {
                                    'post': post,
                                    })
