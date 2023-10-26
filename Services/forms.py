from django import forms
from .models import Service

class ServiceForm(forms.ModelForm):
    AVAILABILITY_CHOICES = [
        (True, 'Disponible'),
        (False, 'No disponible'),
    ]

    availability = forms.ChoiceField(
        choices=AVAILABILITY_CHOICES,
        widget=forms.Select,  # O utiliza Select si prefieres una lista desplegable.
        initial=True  # Puedes establecer el valor inicial según tus necesidades.
    )

    class Meta:
        model = Service
        fields = ['title', 'description', 'price', 'availability', 'category', 'status']