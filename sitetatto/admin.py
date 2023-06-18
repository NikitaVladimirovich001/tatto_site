from django.contrib import admin

from sitetatto.models import Painter, Image, Comment


@admin.register(Painter)
class PainterAdmin(admin.ModelAdmin):
    exclude = ('id',)

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ('id',)

class CommentAdmin(admin.ModelAdmin):
    exclude = ('id',)

admin.site.register(Comment, CommentAdmin)

