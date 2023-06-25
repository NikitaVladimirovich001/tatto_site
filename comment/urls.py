from django.urls import path
from .views import comment_view

app_name = 'comment'

urlpatterns = [
    path('comment/<int:page_number>/', comment_view, name='comments'),
]

