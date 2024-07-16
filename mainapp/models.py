from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

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
