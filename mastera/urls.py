from django.urls import path
from .views import painter_list, painter_detail

urlpatterns = [
    path('mastera/', painter_list.as_view(), name='painter_list'),
    path('mastera/<int:painter_id>/', painter_detail, name='painter_detail'),
]