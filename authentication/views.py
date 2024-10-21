# views.py
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import CustomUser
from .serializer import UserSerializer

from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data.get('role')
            if role == '1':
                user.is_superuser = True
                user.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = CustomUser.get_by_email(email)
            if user is not None and user.check_password(password):
                login(request, user)
                if user.role == 0:
                    return redirect('home_guest')
                elif user.role == 1:
                    return redirect('home_librarian')
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


def home_librarian_view(request):
    return render(request, 'home_librarian.html')


def home_guest_view(request):
    return render(request, 'home_guest.html')


def logout_view(request):
    logout(request)
    return redirect('login')


class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer