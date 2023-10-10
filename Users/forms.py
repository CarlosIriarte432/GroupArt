from django import forms
from .models import User, UserType

class UserRegistrationForm(forms.ModelForm):
    user_type = forms.ModelChoiceField(queryset=UserType.objects.all())

    class Meta:
        model = User
        fields = ['username', 'password', 'full_name', 'rut', 'email', 'phone', 'address', 'privacy_settings']
        widgets = {
            'password': forms.PasswordInput(),
        }
