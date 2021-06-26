from django.db import models
from django.conf import settings


# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=20)
    content = models.ImageField(upload_to='animals', blank=True, null=True)
    tune = models.CharField(max_length=100)


class PictureInfo(models.Model):
    text = models.TextField(blank=True)
    picture = models.OneToOneField(Pictures, on_delete=models.CASCADE)


class PictureUpgrade(models.Model):
    name = models.CharField(max_length=100, unique=True)
    matrix = models.JSONField(default=dict)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)
    tune = models.CharField(max_length=100)

