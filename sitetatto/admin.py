from django.contrib import admin

from sitetatto.models import Painter, Image


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    exclude = ('id',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ('id',)


