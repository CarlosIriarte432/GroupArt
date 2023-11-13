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
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views
from Users import views as Users_views
from Services import views as Services_views
from SocialMedia import views as SocialMedia_views
from Services.views import ServiceCreateView  # Importación local de ServiceCreateView
from Services.views import service_list  # Importación local de service_list
from Services.views import service_detail  # Importación local de service_list
from Services.views import lista_de_servicios  # Importación local de lista_de_servicios
from payment.views import Payment # Importación local de create_payment
from Services.views import return_pay # Importación local de return_pay
from Services.views import confirm_pay # Importación local de confirm_pay
from Services.views import return_last_user_token # Importación local de return_last_user_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Users_views.index, name='index'),
    path('user-login', Users_views.login_view, name='login_view'),
    path('home', Users_views.home, name='home'),
    path('ver-perfil', Users_views.profile, name='profile'),
    path('logout/', Users_views.custom_logout, name='custom_logout'),  
    path('accounts/', include('django.contrib.auth.urls')),
    path('registro/', Users_views.register_user, name='registro_usuario'),
    path('eliminar-cuenta/', Users_views.delete_account, name='delete_account'),
    path('editar-perfil/', Users_views.edit_profile, name='edit_profile'),
    path('reset_password/', Users_views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('services/create/', ServiceCreateView.as_view(), name='service-create'),
    path('services/', service_list, name='service-list'),
    path('my_services/', lista_de_servicios, name='lista_de_servicios'),
    path('services/<int:service_id>/', service_detail, name='service-detail'),
    path('editar-servicio/<int:service_id>/', Services_views.edit_service, name='edit-service'),  
    path('eliminar-servicio/<int:service_id>/', Services_views.delete_service, name='delete-service'),
    path('wall/', SocialMedia_views.wall, name='wall'),
    path('create_post/', SocialMedia_views.create_post, name='create_post'),
    # path('Payment/<int:amount>/<str:email>/<str:subject>/<int:commerce_order>', Payment.create_payment, name='create-payment'),
    path('Payment', Payment.create_payment, name='create-payment'),
    path('Payment/update', Payment.update_state_order, name='update-state-order'),
    path('services/return_pay', return_pay, name='return-pay'),
    path('services/confirm_pay', confirm_pay, name='confirm-pay'),
    path('services/', return_last_user_token, name='return-last-user-token'),
    path('edit-post/<int:post_id>/', SocialMedia_views.edit_post, name='edit-post'),
    path('delete-post/<int:post_id>/', SocialMedia_views.delete_post, name='delete-post'),
    # path('rate-service/<int:service_id>/', Services_views.rate_service, name='rate-service'),
]
