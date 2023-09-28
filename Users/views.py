from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django import forms

def login(request):
    # Lógica de la vista
    return render(request, 'index')

def index(request):
    # Lógica de la vista
    return render(request, 'index.html')

def register(request):
    # Lógica de la vista
    return render(request, 'index.html')

def logout(request):
    # Lógica de la vista
    return redirect(request, 'registration/login.html')
