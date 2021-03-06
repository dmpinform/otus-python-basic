import json

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from jcrosbot import getimage

from io import BytesIO, StringIO
from django.core.files.base import ContentFile

from .models import Pictures, PictureUpgrade
from .tasks import save_pictures_task
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import PictureForm, PictureFormUpgrade, MyUserCreationForm
from django.template.defaulttags import register
from .models import MyUser
from django.contrib.auth.views import LoginView, LogoutView
from loguru import logger

@register.filter
def get_range(value):
    return range(value)


'''На классах CBV generic'''


class PictureListView(ListView):
    model = Pictures
    template_name = 'picpart/index.html'

    def get_queryset(self):
        print(self.request.user)
        return Pictures.objects.filter(user=self.request.user.id)


class PictureDetailView(DetailView):
    model = Pictures
    template_name = 'picpart/detail.html'


class PictureUpdateView(UpdateView):
    model = Pictures
    template_name = 'picpart/edit.html'
    success_url = '/'
    form_class = PictureForm


class PictureCreateView(CreateView):
    model = Pictures
    template_name = 'picpart/edit.html'
    success_url = '/'
    # fields = '__all__'
    form_class = PictureForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PictureDeleteView(DeleteView):
    model = Pictures
    template_name = 'picpart/delete_confirm.html'
    success_url = '/'


class FavoriteView(ListView):
    model = PictureUpgrade
    template_name = 'picpart/favorite.html'
    success_url = '/'

    def get_queryset(self):
        # print(self.request.user)
        return PictureUpgrade.objects.filter(picture__user__id=self.request.user.id)


class ActionView(DetailView):
    model = PictureUpgrade
    template_name = 'picpart/action.html'
    success_url = '/'


class PictureUpgradeDeleteView(DeleteView):
    model = PictureUpgrade
    template_name = 'picpart/delete_confirm.html'
    success_url = '/'

    def get_success_url(self, **kwargs):
        return reverse("detail", kwargs={'pk': self.object.picture.id})


def gen_form(form):
    picture = Pictures.objects.filter(id=form.instance.picture.id)
    file_content = picture.first().content.read()

    width = form.instance.width
    int_color = form.instance.color_limit
    size_part = form.instance.size_part
    hard = form.instance.hard
    image = getimage.img(width, intcolor=int_color, cl=size_part, byte_image=BytesIO(file_content), hard=hard)

    data = json.loads(image[1])
    x = data["x"]
    y = data["y"]
    answers = data["answers"]
    size = data["size"]

    form.instance.x = x
    form.instance.y = y
    form.instance.answers = answers
    form.instance.size = size
    # НУЖНО предупреждение "Сбросится разгадывание"!!!
    form.instance.state = answers

    image = Image.open(BytesIO(image[0]))

    buffer = BytesIO()
    image.save(fp=buffer, format='JPEG')
    pillow_image = ContentFile(buffer.getvalue())
    # image.show()

    form.instance.content.save("name_img", InMemoryUploadedFile(
        pillow_image,  # file
        None,  # field_name
        "name_img",  # file name
        'image/png',  # content_type
        pillow_image.tell,  # size
        None)  # content_type_extra
                               )
    return form


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
        return super().form_valid(gen_form(form))

    def get_success_url(self, **kwargs):
        # переход на все картинки
        # return reverse("detail", kwargs={'pk': self.picture.pk})
        # переход к текущей
        return reverse("picture_preview", kwargs={'pk': self.object.id})


class PicturePreviewDetailView(UpdateView):
    model = PictureUpgrade
    template_name = 'picpart/preview_picture.html'
    form_class = PictureFormUpgrade

    def form_valid(self, form):
        return super().form_valid(gen_form(form))

    def get_success_url(self, **kwargs):
        return reverse("picture_preview", kwargs={'pk': self.object.id})


# добавить в фильр пользователя
# https://question-it.com/questions/1009945/dobavlenie-tovarov-v-spisok-zhelanij-dzhango

class UserCreateView(CreateView):
    model = MyUser
    template_name = 'users/create.html'
    success_url = '/'
    form_class = MyUserCreationForm


class AuthView(LoginView):
    template_name = 'users/login.html'
    success_url = '/'


class MyUserLogoutView(LogoutView):
    pass


def update_state(request):
    if request.method == 'POST':
        picture_id = request.POST["id"]
        picture = PictureUpgrade.objects.get(pk=picture_id)

        state = set(picture.state)
        cell = set(json.loads(request.POST["cell"]))

        for ce in cell:
            if ce in state:
                state.remove(ce)
            else:
                state.add(ce)

        picture.state = list(state)
        picture.save()

        return HttpResponse(200)
    return HttpResponse(404)


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
