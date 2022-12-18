from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegistrationForm, UserLoginForm
from .models import MyUser

def account_register(request):

    if request.user.is_authenticated:
        return redirect('account:profile')

    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save(commit=False)
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.save()

            user = authenticate(request, username=user.username, password = request.POST['password'])
            return redirect('bookstore:home')
        else:
            return HttpResponse('Ошибка обработки данных', status=400)
    else:
        register_form = RegistrationForm()
    return render(request, 'account/registration/register.html', {'form': register_form})


def account_login(request):

    if request.user.is_authenticated:
        return redirect('account:profile')

    if request.POST.get('submit') == 'login':
        login_form = UserLoginForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('account:profile_user')
            else:
                return HttpResponse('Аккаунт не активен')
        else:
            return HttpResponse('Что-то пошло не так') 
    else:
        login_form = UserLoginForm()
    return render(request, 'account/login.html', {'form': login_form})


def profile(request):
    return render(request, 'account/profile/profile.html', {})



