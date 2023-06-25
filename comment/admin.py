from django.contrib import admin
from comment.models import Comments


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name','create_date',)
    readonly_fields = ('create_date',)
    search_fields = ('name','text',)
    list_filter= ('create_date',)
