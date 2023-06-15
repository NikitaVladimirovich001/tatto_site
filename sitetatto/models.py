from django.db import models
from django.contrib.auth.models import User

class Painter(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=1000)
    avatar = models.ImageField(upload_to='%y/%m/%d')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class Image(models.Model):
    name = models.CharField(max_length=32)
    image = models.ImageField(upload_to='images/%y/%m/%d')
    painter = models.ForeignKey(Painter, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

