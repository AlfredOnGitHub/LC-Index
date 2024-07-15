from django.shortcuts import render, redirect
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Agregar aquí la lógica para la autenticación del usuario
        
        messages.success(request, '¡Inicio de sesión exitoso!')
        return redirect('next_page')
    
    return render(request, 'mainapp/index.html')
    return render(request, 'mainapp/index.html')

def next_page(request):
    return render(request, 'mainapp/next_page.html')
