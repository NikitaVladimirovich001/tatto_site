from django.urls import path
from . import views

urlpatterns = [
    path('', views.PainterListView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
    path('tatto/', views.tatto, name='tatto'),
    path('correction/', views.correction, name='correction'),
    path('removal/', views.removal, name='removal'),
]

