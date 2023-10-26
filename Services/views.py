from django.shortcuts import render, redirect
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