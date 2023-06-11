from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from user.models import User
from django import forms

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Пароль'}))
    class Meta:
        model = User
        fields = ('username','password')

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите логин'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'id': 'user', 'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'id': 'pass', 'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password1', 'password2')