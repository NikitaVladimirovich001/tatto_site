from django.db import models


class Painter(models.Model): # Тату-мастер
    name = models.CharField(max_length=64, verbose_name="Мастер")
    description = models.TextField(max_length=1000)
    avatar = models.ImageField(upload_to='%y/%m/%d')

    class Meta:
        ordering = ['name',]
        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'


    def __str__(self):
        return self.name

class Image(models.Model): # Изображения к которым привязан тату-мастер
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)

    class Meta():
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.name
