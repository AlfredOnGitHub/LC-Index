from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

class Organization(models.Model):
    ###############
    # Descripción: Modelo que extiende al usuario de Django para incluir información adicional de la organización, como la foto.
    # User: Modelo de usuario de Django al que se asocia esta organización.
    ###############
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.user.username} Organization'

@receiver(post_save, sender=User)
def create_org_profile(sender, instance, created, **kwargs):
    if created:
        Organization.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_org_profile(sender, instance, **kwargs):
    instance.organization.save()


class Socio(models.Model):
    ###############
    # Descripción: Modelo que extiende al usuario de Django para incluir información adicional de los socios.
    ###############
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='socio')
    photo = models.ImageField(upload_to='profile_pics', blank=True)
    renewal_date = models.DateField(default=timezone.now)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    history = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    NIF = models.TextField()
    email = models.EmailField()
    first_name = models.TextField()
    last_name = models.TextField()

    def __str__(self):
        return self.user.username
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
