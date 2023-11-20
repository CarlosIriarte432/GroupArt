from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    AVAILABILITY_CHOICES = [
        (True, 'Disponible'),
        (False, 'No disponible'),
    ]

    availability = forms.ChoiceField(
        choices=AVAILABILITY_CHOICES,
        widget=forms.HiddenInput, 
        initial=True  
    )

    date = forms.DateField(
        widget=forms.HiddenInput,
        label='Fecha',  
        required=False 
    )

    class Meta:
        model = Service
        fields = ['title', 'description', 'price', 'availability', 'category', 'status', 'date']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'price': 'Precio',
            'status': 'Estado',
        }

class ServiceEditForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'price', 'description', 'category']   
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'price': 'Precio',
            'category': 'Estado',
        }     