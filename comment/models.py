from django.db import models

class Comments(models.Model):
    name = models.CharField(max_length=32,verbose_name='Ваше имя:')
    text = models.TextField(blank=False,verbose_name='Текст отзыва:')
    create_date = models.DateTimeField(auto_now=True,verbose_name='Дата')
    status = models.BooleanField(verbose_name='Видимость статьи', default=False)

    class Meta():
        ordering = ["-id"]
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (self.text[:20] +"...")
