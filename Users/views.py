from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from email import message

# app_name/views.py
from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .models import User, UserType, PrivacySettings
from .forms import UserRegistrationForm  

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data.get('remember_me', False)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecciona a la página de inicio o a donde desees después del inicio de sesión
                return redirect('index')
            else:
                # Agregar un mensaje de error
                messages.error(request, 'El nombre de usuario o la contraseña son incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def index(request):
    # Lógica de la vista
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_type_id = request.POST['user_type']  # Obtén el valor del tipo de usuario seleccionado en el formulario
            user_type = get_object_or_404(UserType, pk=user_type_id)  # Obtiene la instancia de UserType
            user = user_form.save(commit=False)
            user.user_type = user_type  # Asigna la instancia de UserType
            user.save()
    else:
        user_form = UserRegistrationForm()


    return render(request, 'registration/register.html', {'user_form': user_form})


def custom_logout(request):
    logout(request)
    return redirect('/')