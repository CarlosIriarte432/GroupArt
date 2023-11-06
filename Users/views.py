from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
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
            return redirect('user-login')

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