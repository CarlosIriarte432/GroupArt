from django.db import models

from Users.models import UserProfile

# Create your models here.
class payment(models.Model):
    order = models.IntegerField(20)
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='payments')
    token = models.CharField(max_length=60)
    status = models.IntegerField(3)