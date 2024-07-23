from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from .forms import RegisterForm, RegisterSocioForm
from .models import Organization, Socio
from PIL import Image


def index(request):
    ###############
    # Descripción: Vista para manejar la página de inicio y el proceso de autenticación de usuarios.
    # request: Objeto HttpRequest que contiene los datos de la solicitud.
    ###############
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Verificar las credenciales del usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Si las credenciales son válidas, iniciar sesión y redirigir
            login(request, user)
            messages.success(request, '¡Inicio de sesión exitoso!')
            return redirect('next_page')
        else:
            # Si las credenciales no son válidas, mostrar mensaje de error
            messages.error(request, 'El usuario y/o la contraseña no son correctas, o el usuario que se indica no se encuentra registrado.')

    return render(request, 'mainapp/index.html')

@login_required
def next_page(request):
    return render(request, 'mainapp/next_page.html')

def register(request):
    ###############
    # Descripción: Vista para manejar el registro de nuevos usuarios y el envío de un correo electrónico de activación.
    # request: Objeto HttpRequest que contiene los datos de la solicitud.
    ###############
    if request.method == 'POST':
        print("Oli")
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            if 'photo' in request.FILES:
                print("Print") 
                organization = Organization.objects.get(user=user)
                organization.photo = request.FILES['photo']
                organization.save()
                resize_image(organization.photo.path, 100, 100)
            current_site = get_current_site(request)
            mail_subject = 'Active su cuenta.'
            message = render_to_string('mainapp/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            send_mail(mail_subject, message, settings.DEFAULT_FROM_EMAIL, [to_email])
            messages.success(request, 'Por favor, confirme su correo electrónico para completar el registro.')
            return redirect('index')
        else:
            messages.error(request, 'Por favor, corrija los errores en el formulario.')
    else:
        form = RegisterForm()
    return render(request, 'mainapp/register.html', {'form': form})

def resize_image(image_path, width, height):
    ###############
    # Descripción: Redimensiona una imagen a las dimensiones especificadas.
    # image_path: Ruta del archivo de imagen que se va a redimensionar.
    # width: Ancho deseado de la imagen redimensionada.
    # height: Altura deseada de la imagen redimensionada.
    ###############
    img = Image.open(image_path)
    img = img.resize((width, height))
    img.save(image_path)

def activate(request, uidb64, token):
    ###############
    # Descripción: Vista para manejar la activación de la cuenta del usuario a través del enlace enviado por correo electrónico.
    # request: Objeto HttpRequest que contiene los datos de la solicitud.
    # uidb64: ID del usuario codificado en base64.
    # token: Token de activación generado para el usuario.
    ###############
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Su cuenta ha sido activada exitosamente. Ahora puede iniciar sesión.')
        return redirect('index')
    else:
        messages.error(request, 'El enlace de activación no es válido.')
        return redirect('index')
    
@login_required
def perfil_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    return render(request, 'mainapp/perfil_socio.html', {'socio': socio})

def register_socio(request):
    if request.method == 'POST':
        form = RegisterSocioForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirigir a la página de inicio después del registro
    else:
        form = RegisterSocioForm()
    return render(request, 'mainapp/registro_socio.html', {'form': form})