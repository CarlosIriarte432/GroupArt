
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from Users.models import UserProfile

# Modelo de Usuarios

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.timestamp}'
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.post}'



# Modelo de Activity Logs
class ActivityLog(models.Model):
    activity_type = models.CharField(max_length=50)
    activity_date_time = models.DateTimeField()
    involved_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logs')
    activity_description = models.TextField()

# Modelo de Categorías de Publicaciones
class PostCategory(models.Model):
    category_name = models.CharField(max_length=50)
    category_description = models.TextField()

# Modelo de Etiquetas o Tags para Servicios y Publicaciones
class Tag(models.Model):
    tag_name = models.CharField(max_length=50)


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
    recipient_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_recep')


# Modelo de Support Messages
class SupportMessage(models.Model):
    support_message_content = models.TextField()
    support_message_date_time = models.DateTimeField()
    sender_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_support_messages')
    receiver_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_support_messages')

# Modelo de Content Type
class ContentType(models.Model):
    content_type_name = models.CharField(max_length=50)
    
# Modelo de TagsServicePosts (para relacionar etiquetas con servicios o publicaciones)






