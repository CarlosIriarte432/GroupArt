
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


# Modelo de Tipos de Usuario
class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type_name

# Agregar los tipos de usuario por defecto
UserType.objects.get_or_create(user_type_name="Tipo de Usuario 1")
UserType.objects.get_or_create(user_type_name="Tipo de Usuario 2")

# Modelo de Configuraciones de Privacidad
class PrivacySettings(models.Model):
    privacy_options = models.TextField()

# Agregar las opciones de privacidad por defecto
PrivacySettings.objects.get_or_create(privacy_options="Opción 1, Opción 2, Opción 3")

# Modelo de Roles
class Role(models.Model):
    role_name = models.CharField(max_length=50)
    role_description = models.TextField()

# Modelo de Permisos
class Permission(models.Model):
    permission_name = models.CharField(max_length=50)
    permission_description = models.TextField()

# Modelo de Usuarios-Roles (para asignar roles a usuarios)
class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

# Modelo de Roles-Permisos (para asignar permisos a roles)
class RolePermissions(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class RegistroLogin(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateField()

    def __str__(self):
        return f'{self.usuario.username} - {self.fecha}'