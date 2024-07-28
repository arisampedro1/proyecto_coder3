from django import forms
from .models import Empresa, Ubicacion, Contacto, Dueño

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razon_social', 'cuil', 'nombre_de_fantasia', 'actividad_comercial']

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ['nombre', 'apellido']

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['Tel', 'email', 'Tel_alternativo']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['direccion', 'localidad', 'ciudad', 'pais']

class SujetoForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)