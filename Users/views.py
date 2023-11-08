import base64, binascii
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .forms import UserRegisterForm
from .forms import LoginForm
from .models import UserProfile


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data.get('remember_me', False)

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirecciona a la página de inicio o a donde desees después del inicio de sesión
                return redirect('home')
            else:
                # Agregar un mensaje de error
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
            
            # Aquí puedes crear el perfil de usuario
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
    user = request.user  # Obtén el usuario actual
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tus datos se han actualizado con éxito.')
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página de perfil o donde desees
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
            # Genera el token y envía el correo de recuperación
            self.send_password_reset_email(self.request, user)  # Llama a la función send_password_reset_email
        except get_user_model().DoesNotExist:
            # Usuario no encontrado, maneja este caso
            pass
        return super().form_valid(form)

    def send_password_reset_email(self, request, user):
        # Genera el token de restablecimiento de contraseña
        token = default_token_generator.make_token(user)
        user_id = str(user.pk)
        uid = base64.b64encode(user_id.encode()).decode()
        print(f"El uid es: {uid}")
        current_site = get_current_site(request)
        reset_url = f"{current_site.domain}/reset_password/confirm/{uid}/{token}/"

        # Crea el cuerpo del mensaje de correo electrónico utilizando un template
        context = {
            'user': user,
            'reset_url': reset_url,
        }
        email_body = render_to_string('registration/password_reset_email.html', context)

        # Envía el correo electrónico (Debes implementar la función get_gmail_service() correctamente)
        service = self.get_gmail_service()  # Llama a la función en el contexto de la clase
        message = {
            'raw': base64.urlsafe_b64encode(email_body.encode()).decode('utf-8')
        }
        try:
            service.users().messages().send(userId='me', body=message).execute()    # pylint: disable=maybe-no-member
            print('Correo de recuperación de contraseña enviado con éxito')
        except Exception as e:
            print(f'Error al enviar el correo de recuperación: {str(e)}')




    def get_gmail_service(self):
        credentials_path = './credencial.json'

        credentials = service_account.Credentials.from_service_account_file(
            credentials_path, scopes=['https://www.googleapis.com/auth/gmail.send']
        )

        service = build('gmail', 'v1', credentials=credentials)

        return service