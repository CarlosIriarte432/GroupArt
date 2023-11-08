
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from Users.models import UserProfile

# Modelo de Service Categories
class ServiceCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()

    def __str__(self):
        return self.category_name

# Modelo de Service Statuses
class ServiceStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name

# Modelo de Service
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField()
    date = models.DateField(verbose_name='Fecha', null=True, blank=True,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE, default=None, null=True) 
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    status = models.ForeignKey(ServiceStatus, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User
from Services.models import Service

class ServiceRequest(models.Model):
    # Estados posibles
    CREATED = 'Creada'
    ACCEPTED = 'Aceptada'
    CANCELED = 'Cancelada'
    REQUEST_STATUS_CHOICES = [
        (CREATED, 'Creada'),
        (ACCEPTED, 'Aceptada'),
        (CANCELED, 'Cancelada'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_requests')
    request_text = models.TextField()
    request_status = models.CharField(max_length=10, choices=REQUEST_STATUS_CHOICES, default=CREATED)
    created_at = models.DateTimeField(auto_now_add=True)  # Campo para la fecha y hora de creación

    def __str__(self):
        return f'Solicitud para {self.service.title} de {self.author.username}'


# Modelo de Configuraciones de Privacidad
class PrivacySettings(models.Model):
    privacy_options = models.TextField()

# Modelo de Tipos de Usuario
class UserType(models.Model):
    user_type_name = models.CharField(max_length=50)
    
# Modelo de Transacciones
class Transaction(models.Model):
    transaction_date = models.DateTimeField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    client_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

# Modelo de Calificaciones y Comentarios
class RatingAndComment(models.Model):
    rating_score = models.PositiveIntegerField()
    comment = models.TextField()
    client_user = models.ForeignKey(User, on_delete=models.CASCADE)
    provider_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_ratings')
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

# Modelo de Activity Logs
class ActivityLog(models.Model):
    activity_type = models.CharField(max_length=50)
    activity_date_time = models.DateTimeField()
    involved_user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_description = models.TextField()

# Modelo de Categorías de Publicaciones
class PostCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()

# Modelo de Etiquetas o Tags para Servicios y Publicaciones
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

# Modelo de Conversaciones
class Conversation(models.Model):
    conversation_title = models.CharField(max_length=100, blank=True, null=True)  # Opcional

# Modelo de Mensajes
class Message(models.Model):
    message_content = models.TextField()
    message_date_time = models.DateTimeField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

# Modelo de Contenido Multimedia
class Multimedia(models.Model):
    content_type = models.ForeignKey('ContentType', on_delete=models.CASCADE)
    file_path = models.CharField(max_length=255)
    related_metadata = models.TextField()

# Modelo de Notifications
class Notification(models.Model):
    notification_type = models.CharField(max_length=50)
    notification_content = models.TextField()
    notification_date_time = models.DateTimeField()
    recipient_user = models.ForeignKey(User, on_delete=models.CASCADE)

# Modelo de Service History
class ServiceHistory(models.Model):
    completion_date = models.DateTimeField()
    completion_status = models.CharField(max_length=50)
    completion_comment = models.TextField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

# Modelo de Purchases and Billing
class Purchase(models.Model):
    purchase_date = models.DateTimeField()
    billing_details = models.TextField()

# Modelo de Problem Reports
class ProblemReport(models.Model):
    problem_description = models.TextField()
    report_date = models.DateTimeField()
    provider_user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

# Modelo de Support Messages
class SupportMessage(models.Model):
    support_message_content = models.TextField()
    support_message_date_time = models.DateTimeField()
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_support_messages')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_support_messages')

# Modelo de Content Type
class ContentType(models.Model):
    content_type_name = models.CharField(max_length=50)
    
# Modelo de TagsServicePosts (para relacionar etiquetas con servicios o publicaciones)
class TagsServicePosts(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    service_post = models.ForeignKey('Service', on_delete=models.CASCADE)

# Otros modelos...



# Otros modelos...

# Modelo de Datos de Análisis
class AnalyticsData(models.Model):
    analytics_data = models.TextField()
    analysis_date_time = models.DateTimeField()
    involved_user = models.ForeignKey(User, on_delete=models.CASCADE)
    analysis_description = models.TextField()

# Otros modelos...
