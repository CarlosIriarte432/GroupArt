from email import message
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import User, UserType, PrivacySettings
from .forms import UserRegistrationForm  # Deberás crear este formulario


def login(request):
    # Lógica de la vista
    return render(request, 'index.html')

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


def logout(request):
    # Lógica de la vista
    return redirect(request, 'registration/login.html')
