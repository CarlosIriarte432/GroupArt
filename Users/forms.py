# app_name/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Ingrese su email")
    password = forms.CharField(widget=forms.PasswordInput, label="Ingrese su contraseña")
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput, label="Recuérdame")



class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label= 'Nombre de usuario',)
    full_name = forms.CharField(label= 'Nombre completo',max_length=100)
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir contraseña', widget=forms.PasswordInput)
    rut = forms.CharField(label= 'Rut',max_length=20)
    email = forms.EmailField(label= 'Correo electrónico',)
    phone = forms.CharField(label= 'Número de celular',max_length=20)
    address = forms.CharField(label= 'Dirección',)


    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'full_name', 'rut', 'phone', 'address']
        help_texts = {k:"" for k in fields}


