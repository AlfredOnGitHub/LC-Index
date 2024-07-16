from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from mainapp.models import Organization

class Command(BaseCommand):
    ###############
    # Descripción: Crea organizaciones para usuarios existentes
    # BaseCommand: Requerimiento base para la creación del objeto Command.
    ###############

    def handle(self, *args, **kwargs):
        users_without_org = User.objects.filter(organization__isnull=True)
        for user in users_without_org:
            Organization.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f'Organización creada para el usuario {user.username}'))
