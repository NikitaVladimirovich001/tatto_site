from django.shortcuts import render, HttpResponseRedirect
from user.models import User
from user.forms import UserLoginForm, UserRegistrationForm
from django.contrib import auth
from django.urls import reverse
def user(request):# Авторизация
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_superuser:
                return HttpResponseRedirect('/admin/')
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('sitetatto/')
    else:
        form = UserLoginForm()
    context = {'form': UserLoginForm()}
    return render(request, 'user/user.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)
    success_message = 'Вы успешно зарегестрированы!'

