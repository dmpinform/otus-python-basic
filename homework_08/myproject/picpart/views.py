from django.http import Http404
from django.shortcuts import render
from .models import Pictures, PictureUpgrade
from .tasks import save_pictures_task
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView
from .forms import PictureForm

'''На классах CBV generic'''


class PictureListView(ListView):
    model = Pictures
    template_name = 'picpart/index.html'
    # добавить пагинацию на странице
    # paginate_by = 10


class PictureDetailView(DetailView):
    model = Pictures
    template_name = 'picpart/detail.html'


class PictureUpdateView(CreateView):
    model = Pictures
    template_name = 'picpart/edit.html'
    success_url = '/'
    fields = '__all__'
    #form_class = PictureForm

'''На функциях'''


def index_view(request):
    pictures = Pictures.objects.all()
    if request.method == 'POST':
        # запустить RabbitMQ
        # save_pictures_task.delay()
        send_mail('Subject here', 'Here is the message.', 'from@example.com',
                  ['dmpinform@gmail.com'], fail_silently=False)
    return render(request, 'picpart/index.html', {'pictures': pictures})


def detail_view(request):
    picture_id = request.GET["picture_id"]
    picture = Pictures.objects.get(pk=picture_id)
    return render(request, 'picpart/detail.html', {'picture': picture})


def about_view(request):
    return render(request, 'picpart/about.html')



