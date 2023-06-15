from django.urls import path
from . import views
from .views import comment_list

urlpatterns = [
    path('', views.PainterListView.as_view(), name='home'),
]

