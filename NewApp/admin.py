from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Empresa,Dueño,Ubicacion,Contacto
admin.site.register(Empresa)
admin.site.register(Dueño)
admin.site.register(Ubicacion)
admin.site.register(Contacto)