from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, Group, AbstractUser


# Create your models here.
class Pictures(models.Model):
    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=20)
    content = models.ImageField(upload_to='picpart', blank=True, null=True)
    tune = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


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
    color_limit = models.PositiveSmallIntegerField(default=120, blank=False, null=False,
                                                   validators=[MaxValueValidator(255), MinValueValidator(0)])
    width = models.PositiveSmallIntegerField(default=800, blank=False, null=False,
                                             validators=[MaxValueValidator(2000), MinValueValidator(100)])
    hard = models.PositiveSmallIntegerField(default=0, blank=False, null=False,
                                            validators=[MaxValueValidator(100), MinValueValidator(0)])
    favorite = models.BooleanField(default=False, blank=True, null=True)

    x = models.JSONField(default=list, null=True)
    y = models.JSONField(default=list, null=True)
    answers = models.JSONField(default=list, null=True)
    size = models.JSONField(default=list, null=True)
    state = models.JSONField(default=list, null=True)


class MyUser(AbstractUser):
    age = models.PositiveIntegerField(default=18)
