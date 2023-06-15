from django import forms
from django import forms as dj_forms


class ContactForm(forms.Form):
    name = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите имя'}))
    nomer = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите номер телефона'}))
    email = forms.IntegerField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите адрес эл. почты'}))
    date = forms.IntegerField(widget=forms.DateInput(attrs={'id': 'user', 'placeholder': 'Введите дату'}))
    time = forms.IntegerField(widget=forms.TimeInput(attrs={'id': 'user', 'placeholder': 'Введите время'}))

