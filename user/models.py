from django.db import models

class User(models.Model):
    username = models.CharField(max_length=30, verbose_name='Логи')
    password = models.CharField(max_length=30, verbose_name='Пароль')

    def __str__(self):
        return self.username