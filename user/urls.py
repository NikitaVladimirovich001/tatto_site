from django.urls import path, include
from user.views import user, register


urlpatterns = [
    path('', user, name='user'),
    path('register/', register, name='register')
]
