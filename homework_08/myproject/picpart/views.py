from django.http import Http404
from django.shortcuts import render
from .models import Pictures, PictureUpgrade
from .tasks import save_pictures_task
from django.core.mail import send_mail


def index_view(request):

    pictures = Pictures.objects.all()
    if request.method == 'POST':
        # запустить RabbitMQ
        # save_pictures_task.delay()
        send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  ['dmpinform@gmail.com'], fail_silently=False)

    return render(request, 'picpart/index.html', {'pictures': pictures})


def upgrade_view(request):
    picture_id = request.GET["picture_id"]
    picture = Pictures.objects.get(pk=picture_id)
    return render(request, 'picpart/upgrade.html', {'picture': picture})


def load_image_view(request):
    return render(request, 'шаблон')
