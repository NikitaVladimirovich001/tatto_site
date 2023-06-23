from django.urls import path
from .views import comment_view

urlpatterns = [
    path('comment/<int:page_number>/', comment_view, name='comments'),
]

