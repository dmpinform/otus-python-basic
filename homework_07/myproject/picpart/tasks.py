from celery import shared_task
import time

from picpart.models import Pictures


@shared_task
def save_pictures_task():
    time.sleep(10)
    pictures = Pictures.objects.all()
    with open('pictures.txt', 'w', encoding='utf-8') as f:
        for picture in pictures:
            f.write(f'{picture.name}\n')


