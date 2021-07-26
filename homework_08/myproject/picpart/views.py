
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from jcrosbot import getimage

from io import BytesIO, StringIO
from django.core.files.base import ContentFile

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
        picture = Pictures.objects.filter(id=self.picture.pk)

        # в обработчик передать ----вынести в функцию---
        f = BytesIO()
        try:
            # pillow_img = picture.first().content
            # pillow_img.save(f, format='png')
            #
            # pillow_img = getimage.img(400, intcolor=120, byte_image=f)

            form.instance.content = picture.first().content # ContentFile(f.getvalue())
        finally:
            f.close()

        # -----------------------------

        return super().form_valid(form)

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
        # заменить на изображение из родительской таблицы  Pictures.objects.filter(id=self.picture.pk)
        picture = form.instance.pk
        file_content = picture.read()
        image = getimage.img(form.instance.width, intcolor=120, byte_image=BytesIO(file_content))

        BytesIO(image).getvalue()

        image = Image.open(BytesIO(image))

        buffer = BytesIO()
        image.save(fp=buffer, format='JPEG')
        pillow_image = ContentFile(buffer.getvalue())

        #image.show()

        form.instance.content.save("name_img", InMemoryUploadedFile(
             pillow_image,       # file
             None,               # field_name
             "name_img",           # file name
             'image/png',       # content_type
             pillow_image.tell,  # size
             None)               # content_type_extra
        )

        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse("picture_preview", kwargs={'pk': self.object.id})


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



