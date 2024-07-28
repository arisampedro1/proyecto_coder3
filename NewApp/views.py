from django.shortcuts import render, redirect
from .models import Ubicacion,Contacto,Empresa,Dueño
from NewApp.forms import UbicacionForm, ContactoForm, EmpresaForm, DueñoForm, SujetoForm

def inicio(request):
    return render(request, "NewApp/inicio.html")

def guardarEmpresa(request):
    empresas = Empresa.objects.all()
    return render(request, 'NewApp/guardarEmpresa.html', {'empresa': empresas})

def registrarEmpresa(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guardarEmpresa')
    else:
        form = EmpresaForm()
    return render(request, 'NewApp/registro_de_empresa.html', {'form': form})

def SujetoEmpresa(request):
    form = SujetoForm()
    sujetos = []
    if request.method == 'GET':
        form = SujetoForm(request.GET)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            empresa = empresa.objects.filter(titulo__icontains=nombre)
    return render(request, 'NewApp/SujetoEmpresa.html', {'form': form, 'Sujeto': sujetos})

def guardarDueño(request):
    dueños = Dueño.objects.all()
    return render(request, 'NewApp/guardarDueño.html', {'dueño': dueños})

def registrarDueño(request):
    if request.method == 'POST':
        form = DueñoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guardarDueño')
    else:
        form = DueñoForm()
    return render(request, 'NewApp/registrarDueño.html', {'form': form})

def guardarUbicacion(request):
    ubicaciones = Ubicacion.objects.all()
    return render(request, 'NewApp/guardarUbicacion.html', {'ubicacion': ubicaciones})

def registrarUbicacion(request):
    if request.method == 'POST':
        form = UbicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guardarUbicacion')
    else:
        form = UbicacionForm()
    return render(request, 'NewApp/registrarUbicacion.html', {'form': form})

def guardarContacto(request):
    contactar = Contacto.objects.all()
    return render(request, 'NewApp/guardarContacto.html', {'contactar': contactar})

def registrarContacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guardarContacto')
    else:
        form = ContactoForm()
    return render(request, 'NewApp/registrarContacto.html', {'form': form})