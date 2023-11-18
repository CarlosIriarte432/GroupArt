
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
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)
    avg_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    total_ratings = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

