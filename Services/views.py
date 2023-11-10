from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from .models import Service
from .forms import ServiceForm, ServiceEditForm
from django.contrib.auth.decorators import login_required
from datetime import date  # Importa el módulo date de datetime
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib import messages
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
    query = request.GET.get('q', '')
    services = Service.objects.filter(title__icontains=query)
    
    return render(request, 'services/services.html', {'services': services, 'query': query})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    # Verificar si el usuario autenticado es el creador del servicio
    if service.created_by != request.user.userprofile:
        messages.error(request, "No tienes permiso para editar este servicio.")
        return redirect('service-detail', service_id)

    if request.method == 'POST':
        form = ServiceEditForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service-detail', service_id)

    else:
        form = ServiceEditForm(instance=service)

    return render(request, 'services/edit_service.html', {'service': service, 'form': form})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    # Verificar si el usuario autenticado es el creador del servicio
    if service.created_by != request.user.userprofile:
        messages.error(request, "No tienes permiso para eliminar este servicio.")
        return redirect('service-detail', service_id)

    if request.method == 'POST':
        service.delete()
        return redirect('service-list')

    return render(request, 'services/delete_service.html', {'service': service})