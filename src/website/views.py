from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm


def index(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfuly registered! ')
            return redirect('index')
    else:
        form = SignUpForm()
        return render(request, 'website/index.html', context={'form':form})


def login_user(request):
    pass


def logout_user(request):
    pass
