from django.core.management.base import BaseCommand
from picpart.models import Pictures, PictureUpgrade, PictureInfo


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        print('hello command')
        Pictures.objects.all().delete()

        picture = Pictures.objects.create(name="Первая")
        print(picture.id)
        picture.save()

        picture_info = PictureInfo.objects.create(text="Первая", picture=picture)
        print(picture_info.id)
        picture_info.save()

        picture_upgrade = PictureUpgrade.objects.create(name="Обработка 1", picture=picture)
        print(picture_upgrade.id)
        picture_upgrade.save()
        print('end')

        # Получить всё
        pictures = Pictures.objects.all()
        for picture in pictures:
            print(type(picture))
            print(picture)

        # фильтр - несколько объектов QurySet
        picture_filter = Pictures.objects.filter(name="Первая")
        for picture in picture_filter:
            print(picture.name)

        # один объект Picture
        picture_first = Pictures.objects.filter(name="Первая").first()
        print(picture_first.name)

        # фильтр запрос по ID. Если не найден(или найдено больше 1) то ошибка.
        # обычно запрос по ID
        picture_get = Pictures.objects.get(name="Первая")
        print(picture_get.name)

        # сложные вложенные запросы (parent__ref__ref__ через связи и атрибуты)
        picture = Pictures.objects.filter(pictureinfo__text="Первая")
        print(picture.first().name)

        # найти по контексту
        picture = Pictures.objects.filter(pictureinfo__text__startswith="П")
        name = picture.first().name
        print(picture, name)

        picture = Pictures.objects.filter(pictureinfo__text__contains="вая")
        print(picture.first().name)
