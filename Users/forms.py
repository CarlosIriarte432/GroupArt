# app_name/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Ingrese su email")
    password = forms.CharField(widget=forms.PasswordInput, label="Ingrese su contraseña")
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput, label="Recuérdame")
