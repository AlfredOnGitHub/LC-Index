from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('next/', views.next_page, name='next_page'),
    path('register/', views.register, name='register'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('socio/<str:user>/', views.perfil_socio, name='perfil_socio'),
]
