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
from Users import views as Users_views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', Users_views.login, name='login'),
     path('index', Users_views.index, name='index'),
     path('logout', Users_views.logout, name='logout'),
    # path('register.html', Users_views.register, name='register'),
     path('accounts/', include('django.contrib.auth.urls'))
]