from django import forms
from .models import Empresa, Ubicacion, Contacto, Dueño

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['razon_social', 'cuil', 'nombre_de_fantasia', 'actividad_comercial']
        def clean_cuil(self):
           cuil = self.cleaned_data.get('cuil'),
           if Empresa.objects.filter(cuil=cuil).exists():
                 raise forms.ValidationError('Este cuil ya está registrado. Por favor, elija otro.')
           return cuil

class DueñoForm(forms.ModelForm):
    class Meta:
        model = Dueño
        fields = ['nombre', 'apellido']
        
        def clean_nombre(self):
           nombre = self.cleaned_data.get('nombre'),
           if Dueño.objects.filter(nombre=nombre).exists():
                 raise forms.ValidationError('Este nombre ya está registrado. Por favor, elija otro.')
           return nombre

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['Tel', 'email', 'Tel_alternativo']
        def clean_email(self):
           email = self.cleaned_data.get('email'),
           if Contacto.objects.filter(email=email).exists():
                 raise forms.ValidationError('Este email ya está registrado. Por favor, elija otro.')
           return email

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['direccion', 'localidad', 'ciudad', 'pais']
