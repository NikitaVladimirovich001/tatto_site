from django import forms
from .models import *

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'text')

    name = forms.CharField(max_length=50, min_length=3, label="Ваше имя", widget=forms.TextInput(attrs={'placeholder': 'Кошкин Кот Котович', 'class': 'form_input'}))
    text = forms.CharField(max_length=600, label="Комментарий", widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, 'placeholder': 'Напишите пару слов...', 'class': 'form_input'}))
