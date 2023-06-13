from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username','password')

class UserRegistrationForm(UserCreationForm):
   username = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите логин'}))
   first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите имя пользователя'}))
   email = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите адрес эл. почты'}))
   password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Введите пароль'}))
   password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Подтвердите пароль'}))

