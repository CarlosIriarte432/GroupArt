
# Create your models here.
from django.db import models

# Modelo de Usuarios
class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Almacenar la contraseña encriptada
    full_name = models.CharField(max_length=100)
    rut = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    privacy_settings = models.ForeignKey('PrivacySettings', on_delete=models.CASCADE)
    user_type = models.ForeignKey('UserType', on_delete=models.CASCADE)

# Modelo de Tipos de Usuario
class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)

# Modelo de Configuraciones de Privacidad
class PrivacySettings(models.Model):
    privacy_options = models.TextField()

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

