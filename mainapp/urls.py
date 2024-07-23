from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next/', views.next_page, name='next_page'),
    path('register/', views.register, name='register'),
    path('registro_socio/', views.register_socio, name='registro_socio'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('perfil_socio/<int:id>/', views.perfil_socio, name='perfil_socio'),
]
