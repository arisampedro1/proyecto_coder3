from django.urls import path
from NewApp import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrar-empresa/', views.registrar_empresa, name='registrar_empresa'),
    path('registrar-formulario/', views.registrar_formulario, name='registrar_formulario'),
    path('registrar-ubicacion/', views.registrar_ubicacion, name='registrar_ubicacion'),
    path('registrar-contacto/', views.registrar_contacto, name='registrar_contacto'),
    path('fin/', views.fin, name='fin'), 
     path('buscar-empresas/', views.buscar_empresas, name='buscar_empresas'),
]