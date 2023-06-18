from django.db import models
from django.contrib.auth.models import User
import datetime

class Painter(models.Model): # Тату-мастер
    name = models.CharField(max_length=64, verbose_name="Мастер")
    description = models.TextField(max_length=1000)
    avatar = models.ImageField(upload_to='%y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class Image(models.Model): # Изображения к которым привязан тату-мастер
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model): # Коментарий
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Текст комментария")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
