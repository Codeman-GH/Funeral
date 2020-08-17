from django.contrib import admin
from .models import Tribute, Memory, Photo

# Register your models here.



class TributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'image', 'posted_on' ]


class MemoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'memories', 'message', 'posted_on']


class PhotoAdmin(admin.ModelAdmin):
    list_display = ['name','image', 'posted_on']





admin.site.register(Tribute, TributeAdmin)
admin.site.register(Memory, MemoryAdmin)
admin.site.register(Photo, PhotoAdmin)
