from django.urls import path, include
from . import views

urlpatterns = [
    path('mastera/', views.PaintersList.as_view(), name='mastera'),
    path('painter_detail/', views.painter_detail, name='painter_detail'),
]