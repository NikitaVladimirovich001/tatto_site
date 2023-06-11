from django.shortcuts import render, HttpResponseRedirect
from user.models import User
from user.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
def user(request):# Авторизация
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user =auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('home')
    else:
        form = UserLoginForm()
    context = {'from': UserLoginForm()}
    return render(request, 'user/user.html', context)

def register(request):
    return render(request, 'user/register.html')

