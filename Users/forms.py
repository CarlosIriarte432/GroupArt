# app_name/forms.py
from django import forms
from .models import User, UserType

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label="Ingrese su email")
    password = forms.CharField(widget=forms.PasswordInput, label="Ingrese su contraseña")
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput, label="Recuérdame")


class UserRegistrationForm(forms.ModelForm):
    user_type = forms.ModelChoiceField(queryset=UserType.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'rut', 'email', 'phone', 'address', 'privacy_settings']
        widgets = {
            'password': forms.PasswordInput(),
        }
