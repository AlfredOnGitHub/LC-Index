from django.shortcuts import render, redirect
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
from .forms import RegisterForm

def index(request):
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
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Desactivar cuenta hasta que se verifique el correo
            user.save()
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

def activate(request, uidb64, token):
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