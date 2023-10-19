# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import UserProfile
# from .forms import UserRegisterForm
# from django.contrib.auth.models import User

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         user_form = UserRegisterForm(instance=instance)
        
#         # Asegúrate de que el formulario esté marcado como válido
#         if user_form.is_valid():
#             # Accede a los datos limpios después de que el formulario esté marcado como válido
#             UserProfile.objects.create(
#                 user=instance,
#                 full_name=user_form.cleaned_data['full_name'],
#                 rut=user_form.cleaned_data['rut'],
#                 email=user_form.cleaned_data['email'],
#                 phone=user_form.cleaned_data['phone'],
#                 address=user_form.cleaned_data['address']
#             )