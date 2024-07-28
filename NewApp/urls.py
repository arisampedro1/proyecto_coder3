from django.urls import path
from NewApp import views


urlpatterns = [
    path('', views.inicio, name='start'),
    path('Company/', views.guardarEmpresa, name='save_company'),
    path('Company/register/', views.registrarEmpresa, name='register_company'),
    path('Company/search/', views.SujetoEmpresa, name='search_company'),
    path('Owner/', views.guardarDueño, name='save_owner'),
    path('Owner/register/', views.registrarDueño, name='register_owner'),
    path('Location/', views.guardarUbicacion, name='save_location' ),
    path('Location/register', views.registrarUbicacion, name='register_location'),
    path('Contact/', views.guardarContacto, name='save_contact'),
    path('Contact/register', views.registrarContacto, name='register_location'),
]