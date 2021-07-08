from django.db import models
from django.conf import settings


# Create your models here.
class Pictures(models.Model):
    objects = None
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=20)
    content = models.ImageField(upload_to='picpart', blank=True, null=True)
    tune = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PictureInfo(models.Model):
    text = models.TextField(blank=True)
    picture = models.OneToOneField(Pictures, on_delete=models.CASCADE)


class PictureUpgrade(models.Model):
    name = models.CharField(max_length=100, unique=True)
    matrix = models.JSONField(default=dict)
    content = models.ImageField(upload_to='process', blank=True, null=True)
    picture = models.ForeignKey(Pictures, on_delete=models.CASCADE)
    tune = models.CharField(max_length=100)
    size_part = models.PositiveSmallIntegerField(default=12, blank=False, null=False)
    color_limit = models.PositiveSmallIntegerField(default=100, blank=False, null=False)
    width = models.PositiveSmallIntegerField(default=800, blank=False, null=False)
