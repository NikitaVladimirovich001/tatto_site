from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.PainterListView.as_view(), name='home'),
]
