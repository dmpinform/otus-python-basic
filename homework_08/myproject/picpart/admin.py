from django.contrib import admin
from .models import Pictures, PictureUpgrade, PictureInfo, MyUser

# Register your models here.
admin.site.register(Pictures)
admin.site.register(PictureUpgrade)
admin.site.register(PictureInfo)
admin.site.register(MyUser)
