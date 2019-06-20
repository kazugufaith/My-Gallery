from django.contrib import admin
from .models import Editor,Image,tags
#Register your models here.

class ImageAdmin(admin.ModelAdmin):
    # filter_horizontal =('location',)

    admin.site.register(Editor)
    admin.site.register(Image)
    admin.site.register(tags)
