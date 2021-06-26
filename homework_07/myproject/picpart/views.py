from django.shortcuts import render
from .models import Pictures, PictureUpgrade
# Create your views here.


def index_view(request):
    pictures = Pictures.objects.all()
    return render(request, 'picpart/index.html')


def load_image_view(request):
    return render(request, 'шаблон')
