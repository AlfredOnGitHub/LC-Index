from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Organization, Socio

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

class RegisterSocioForm(forms.ModelForm):
    ###############
    # Descripción: Formulario de registro personalizado para los socios
    ###############
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)
    photo = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'onchange': 'previewImage()'}))
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    NIF = forms.CharField(max_length=9, required=True)

    class Meta:
        ###############
        # Descripción: Define el modelo base (Socio) y los campos que serán incluidos en el formulario.
        ###############
        model = Socio
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'photo', 'NIF']

    def clean_email(self):
        ###############
        # Descripción: Verifica que el correo electrónico no esté ya registrado en la base de datos.
        # self: Instancia del formulario actual, que permite el acceso a sus datos y métodos.
        ###############
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('El correo electrónico ya está en uso.')
        return email

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name']
        )
        socio = super().save(commit=False)
        socio.user = user
        if commit:
            socio.save()
        return socio
