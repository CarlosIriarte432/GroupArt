from sys import setprofile
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView

import Services
from .models import Service
from .forms import ServiceForm, ServiceEditForm
from django.contrib.auth.decorators import login_required
from datetime import date  # Importa el módulo date de datetime
from django.contrib.auth import get_user_model
from .models import UserProfile
from django.contrib import messages
from django.db import connection
User = get_user_model()



class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/service_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user

        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        
        form.instance.created_by = user_profile

        form.instance.date = form.cleaned_data['date']

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('service-list')  
    def get_initial(self):
        initial = super().get_initial()
        initial['date'] = date.today()  
        return initial

def service_list(request):
    query = request.GET.get('q', '')
    services = Service.objects.filter(title__icontains=query)
    
    return render(request, 'services/services.html', {'services': services, 'query': query})
    query = request.GET.get('q', '')
    services = Service.objects.filter(title__icontains=query)
    
    return render(request, 'services/services.html', {'services': services, 'query': query})

def service_detail(request, service_id):
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'services/service_detail.html', {'service': service})


def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if service.created_by != request.user.userprofile:
        messages.error(request, "No tienes permiso para editar este servicio.")
        return redirect('service-detail', service_id)

    if request.method == 'POST':
        form = ServiceEditForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service-list')
            return redirect('service-list')

    else:
        form = ServiceEditForm(instance=service)

    return render(request, 'services/edit_service.html', {'service': service, 'form': form})

def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if service.created_by != request.user.userprofile:
        messages.error(request, "No tienes permiso para eliminar este servicio.")
        return redirect('service-detail', service_id)

    if request.method == 'POST':
        service.delete()
        return redirect('service-list')

    return render(request, 'services/delete_service.html', {'service': service})

def lista_de_servicios(request):
    services = Service.objects.filter(created_by=request.user.userprofile)

    return render(request, 'services/my_services.html', {'services': services})

def lista_de_servicios_contratados(request):
    if request.user.is_authenticated:
        user_id = request.user.id

        query = """
            SELECT s.title, s.description, s.price, s.date, s.order_number, s.id, s.created_by_id, s.status_id, u.full_name, u.phone,
                CASE p.status 
                    WHEN 0 THEN 'Sin Registro'
                    WHEN 1 THEN 'Pendiente de Pago'
                    WHEN 2 THEN 'Pagado' 
                    WHEN 3 THEN 'Rechazado'
                    WHEN 4 THEN 'Anulado'
                END AS payment_status
            FROM Services_service s
            INNER JOIN payment_payment p ON s.order_number = p.order 
            LEFT JOIN Users_userprofile u ON s.user_id = u.user_id
            WHERE p.id_user = %s
        """

        with connection.cursor() as cursor:
            cursor.execute(query, [user_id])
            servicios_contratados = cursor.fetchall()

        column_names = [desc[0] for desc in cursor.description]
        servicios_contratados = [dict(zip(column_names, row)) for row in servicios_contratados]

        return render(request, 'services/contracted_services.html', {'servicios_contratados': servicios_contratados})
    else:
        return render(request, 'path_to_your_template/login.html')  

def return_pay(request):
    return render(request, 'services/return_pay.html')

def confirm_pay(request):
    return render(request, 'services/confirm_pay.html')


def update_status_service(request):
        commerce_order = request.POST.get('commerce_order')
        action = request.POST.get('action')
        response = ""
        print(commerce_order)
        print(action)
        if action == 'cancel':
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Services_service SET status_id = 3 WHERE id = %s", [commerce_order])
                response = cursor.rowcount
        elif action == 'finish':
            with connection.cursor() as cursor:
                cursor.execute("UPDATE Services_service SET status_id = 2 WHERE id = %s", [commerce_order])
                response = cursor.rowcount
        print(response)
        return HttpResponseRedirect('/contracted_services/')
    