from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .models import Service
from .forms import ServiceForm
from django.contrib.auth.decorators import login_required
from datetime import date  # Importa el módulo date de datetime
from django.contrib.auth import get_user_model
from .models import UserProfile

User = get_user_model()



class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        # Obtenemos o creamos el UserProfile asociado al usuario actual
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        
        # Asignamos el UserProfile al campo created_by
        form.instance.created_by = user_profile

        # Asignamos la fecha del formulario al objeto Service
        form.instance.date = form.cleaned_data['date']

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('service-list')  # Reemplaza 'service-list' con el nombre de tu URL de lista de servicios

    def get_initial(self):
        initial = super().get_initial()
        initial['date'] = date.today()  # Establece la fecha inicial en la fecha actual
        return initial

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})

def get_service_details(request, service_id):
    try:
        # Obten los detalles del servicio usando el ID proporcionado
        service = Service.objects.get(id=service_id)
        
        # Crea un diccionario con los detalles del servicio
        service_details = {
            'title': service.title,
            'description': service.description,
            'price': str(service.price),
        }
        
        # Devuelve los detalles en formato JSON
        return JsonResponse(service_details)
    except Service.DoesNotExist:
        return JsonResponse({'error': 'El servicio no existe'}, status=404)
from django.shortcuts import render
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, 'services/services.html', {'services': services})
