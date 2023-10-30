"""
URL configuration for GroupArt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from . import views
from Users import views as Users_views
from SocialMedia import views as SocialMedia_views
from Services.views import ServiceCreateView  # Importación local de ServiceCreateView
from Services.views import service_list  # Importación local de service_list
from Services.views import service_detail  # Importación local de service_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Users_views.index, name='index'),
    path('user-login', Users_views.login_view, name='login_view'),
    path('home', Users_views.home, name='home'),
    path('logout/', Users_views.custom_logout, name='custom_logout'),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', Users_views.register_user, name='registro_usuario'),
    path('eliminar-cuenta/', Users_views.delete_account, name='delete_account'),
    path('editar-perfil/', Users_views.edit_profile, name='edit_profile'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/', service_list, name='service-list'),  
    path('services/<int:service_id>/', service_detail, name='service-detail'),
]
