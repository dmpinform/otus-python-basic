from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# from jcrosbot import getimage

from .models import Pictures, PictureUpgrade
from .tasks import save_pictures_task
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import PictureForm, PictureFormUpgrade

'''На классах CBV generic'''


class PictureListView(ListView):
    model = Pictures
    template_name = 'picpart/index.html'
    # добавить пагинацию на странице
    # paginate_by = 10


class PictureDetailView(DetailView):
    model = Pictures
    template_name = 'picpart/detail.html'


class PictureUpdateView(UpdateView):
    model = Pictures
    template_name = 'picpart/edit.html'
    success_url = '/'
    # fields = '__all__'
    form_class = PictureForm


class PictureCreateView(CreateView):
    model = Pictures
    template_name = 'picpart/edit.html'
    success_url = '/'
    # fields = '__all__'
    form_class = PictureForm


class PictureDeleteView(DeleteView):
    model = Pictures
    template_name = 'picpart/delete_confirm.html'
    success_url = '/'


class PictureUpgradeCreateView(CreateView):
    model = PictureUpgrade
    template_name = 'picpart/upgrade.html'
    success_url = '/'
    form_class = PictureFormUpgrade

    # по self.picture найти картинку в БД и применить фильтры
    # вызвать бота, вернуть картинку в БД и отобразить

    def dispatch(self, request, *args, **kwargs):
        self.picture = get_object_or_404(Pictures, pk=kwargs['picture_id'])
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.picture = self.picture
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        # obj = form.instance or self.object
        # переход на предыдущую
        return reverse("detail", kwargs={'pk': self.picture.pk})
        # переход на текущую
        # return self.request.path


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



