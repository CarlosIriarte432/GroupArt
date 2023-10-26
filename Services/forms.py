from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    AVAILABILITY_CHOICES = [
        (True, 'Disponible'),
        (False, 'No disponible'),
    ]

    availability = forms.ChoiceField(
        choices=AVAILABILITY_CHOICES,
        widget=forms.HiddenInput,  # Utiliza HiddenInput para ocultar el campo
        initial=True  # Establece el valor inicial en 'True' (Disponible)
    )

    date = forms.DateField(
        widget=forms.HiddenInput,
        label='Fecha',  # Cambia la etiqueta según tus necesidades
        required=False  # Si deseas que la fecha sea opcional, establece esto en True
    )

    class Meta:
        model = Service
        fields = ['title', 'description', 'price', 'availability', 'category', 'status', 'date']
        labels = {
            'title': 'Título',
            'description': 'Descripción',
            'price': 'Precio estimado',
            'status': 'Estado',
        }