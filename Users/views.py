import base64
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from .forms import UserRegisterForm
from .forms import LoginForm
from .models import UserProfile
from django.contrib.auth import login
from .models import LoginRecord
from django.db.models import Count
import json
from django.http import HttpResponse
import plotly.graph_objects as go
from xhtml2pdf import pisa
from io import BytesIO
from django.db.models.functions import TruncMonth
from django.contrib.admin.views.decorators import staff_member_required
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data.get('remember_me', False)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_record = LoginRecord(user=user)
                login_record.save()

                login(request, user)

                return redirect('home')
            else:
                messages.error(request, 'El nombre de usuario o la contraseña son incorrectos.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                rut=form.cleaned_data['rut'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
            )
            
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado, Por favor inicie sesión')
            return redirect('login_view')

    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registration/register.html', context)

def custom_logout(request):
    logout(request)
    return redirect('login_view')

@login_required
def delete_account(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = request.user

        if user.check_password(password):
            user.delete()
            messages.success(request, 'Tu cuenta ha sido eliminada con éxito.')
            return redirect('/')
        else:
            messages.error(request, 'La contraseña es incorrecta. Inténtalo de nuevo.')

    return render(request, 'registration/delete_account.html')

@login_required
def edit_profile(request):
    user = request.user  
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos se han actualizado con éxito.')
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = UserRegisterForm(instance=user)
    
    return render(request, 'registration/edit_profile.html', {'form': form})

def profile(request):
    return render(request, 'profile/profile.html')

User = get_user_model()
class CustomPasswordResetView(PasswordResetView):

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = get_user_model().objects.get(email=email)
            print(f'Consulta exitosa. Usuario encontrado: {user}')
            self.send_password_reset_email(self.request, user)  
        except get_user_model().DoesNotExist:
            print(f'Usuario no encontrado con el correo electrónico: {email}')
            pass
        return super().form_valid(form)

    def send_password_reset_email(self, request, user):
        token = default_token_generator.make_token(user)
        user_id = str(user.pk)
        uid = base64.b64encode(user_id.encode()).decode()
        current_site = get_current_site(request)
        reset_url = f"{current_site.domain}/reset_password/confirm/{uid}/{token}/"

        context = {
            'user': user,
            'reset_url': reset_url,
            'uid': uid,
            'token': token,
        }
        email_body = render_to_string('registration/password_reset_email.html', context)

        smtp_server = 'smtp.elasticemail.com'
        smtp_port = 2525
        smtp_username = 'soporte@groupart.com'
        smtp_password = 'F9EEEEE96801CEAFCA1D3FCA14C1A8861CAC'

        msg = MIMEMultipart()
        msg['From'] = 'groupart.soporte@gmail.com'
        msg['To'] = user.email
        msg['Subject'] = 'Recuperación de contraseña'

        msg.attach(MIMEText(email_body, 'html'))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            server.sendmail(msg['From'], msg['To'], msg['email_body'])
            server.quit()
            print('Correo de recuperación de contraseña enviado con éxito')
        except Exception as e:
            print(f'Error al enviar el correo de recuperación: {str(e)}')



@staff_member_required
def login_statistics(request):
    login_count_by_month = LoginRecord.objects.annotate(
        month=TruncMonth('login_time')
    ).values('month').annotate(total=Count('id'))

    total_logins = LoginRecord.objects.count()

    login_count_by_month = list(login_count_by_month)  

    for entry in login_count_by_month:
        entry['month'] = entry['month'].strftime('%Y-%m')

    
    login_count_by_month_json = json.dumps(login_count_by_month)

    return render(request, 'statistics/login_statistics.html', {'login_count_by_month': login_count_by_month_json, 'total_logins': total_logins})

@staff_member_required
def export_plotly_to_pdf(request):
    login_count_by_month = LoginRecord.objects.annotate(
        month=TruncMonth('login_time')
    ).values('month').annotate(total=Count('id'))

    login_count_by_month = list(login_count_by_month)

    for entry in login_count_by_month:
        entry['month'] = entry['month'].strftime('%Y-%m-%d')

    months = [entry['month'] for entry in login_count_by_month]
    counts = [entry['total'] for entry in login_count_by_month]

    fig = go.Figure(data=[go.Bar(x=months, y=counts)])

    fig_html = go.FigureWidget.to_html(fig, full_html=False)

    result = BytesIO()

    pdf = pisa.pisaDocument(BytesIO(fig_html.encode("UTF-8")), result)

    if not pdf.err:
        response = HttpResponse(result.getvalue(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="grafico-logins.pdf"'
        return response

    return HttpResponse("Error al generar el PDF")

def users_created_statistics(request):
    users_created_by_month = User.objects.annotate(
        month=TruncMonth('date_joined')
    ).values('month').annotate(total=Count('id'))

    months = [entry['month'] for entry in users_created_by_month]
    counts = [entry['total'] for entry in users_created_by_month]

    total_users_created = sum(counts)

    data = {
        'months': months,
        'counts': counts,
        'total_users_created': total_users_created
    }

    return JsonResponse(data)