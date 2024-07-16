from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Organization

class RegisterForm(UserCreationForm):
    ###############
    # Descripción: Formulario de registro personalizado que hereda de UserCreationForm e incluye campos adicionales como email y photo.
    # UserCreationForm: Formulario proporcionado por Django para crear usuarios con campos de nombre de usuario y contraseña.
    ###############
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange': 'previewImage()'}))

    class Meta:
        ###############
        # Descripción: Define el modelo base (User) y los campos que serán incluidos en el formulario.
        ###############
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'photo')

    def clean_email(self):
        ###############
        # Descripción: Verifica que el correo electrónico no esté ya registrado en la base de datos.
        # self: Instancia del formulario actual, que permite el acceso a sus datos y métodos.
        ###############
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('El correo electrónico ya está en uso.')
        return email

