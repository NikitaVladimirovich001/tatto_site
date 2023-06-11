from django.db import models

from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='Логи')
    password = models.CharField(max_length=30, verbose_name='Пароль')

    USERNAME_FIELD = 'user'

    def __str__(self):
        return self.username