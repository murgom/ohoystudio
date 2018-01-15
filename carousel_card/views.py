from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from carousel_card.models import CarouselImage, CarouselGalleryImage, CarouselSmsImage

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
