from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm


def login_view(request):
    if request.user.is_authenticated:
        return redirect('calculator')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calculator')
        else:
            messages.error(request, "Usuário ou senha inválidos.")
    else:
        form = AuthenticationForm()
    return render(request, 'authapp/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return render(request, 'authapp/logout.html')


def register_view(request):
    if request.user.is_authenticated:
        return redirect('calculator')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Cadastro realizado com sucesso! Faça login.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'authapp/register.html', {'form': form})
