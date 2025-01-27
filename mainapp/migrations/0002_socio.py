# Generated by Django 5.0.7 on 2024-07-22 07:59

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='profile_pics')),
                ('renewal_date', models.DateField(default=django.utils.timezone.now)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('history', models.TextField(blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('NIF', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='socio', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
