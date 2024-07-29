from django.shortcuts import render, redirect
from .models import Ubicacion,Contacto,Empresa,Dueño
from NewApp.forms import UbicacionForm, ContactoForm, EmpresaForm, DueñoForm
from django.contrib import messages

def inicio(request):
    return render (request, "NewApp/inicio.html")

def registrar_formulario(request):

    if request.method == 'POST':

        dueño = Dueño(nombre=request.POST['nombre'],apellido=request.POST['apellido'])
        dueño.save()

        return render(request, "NewApp/registros/registrar_empresa.html")

    return render(request,"NewApp/registros/registrar_formulario.html")
def registrar_empresa(request):
    if request.method == 'POST':
        empresa = Empresa(
            razon_social=request.POST['razon social'],
            cuil=request.POST['cuil'],
            nombre_de_fantasia=request.POST['nombre de fantasia'],
            actividad_comercial=request.POST['actividad comercial']
        )
        empresa.save()
        messages.success(request, 'Empresa registrada exitosamente.')
        return redirect('registrar_ubicacion') 

    return render(request, "NewApp/registros/registrar_empresa.html")

def registrar_ubicacion(request):
    if request.method == 'POST':
        ubi = Ubicacion(
            direccion=request.POST['direccion'],
            localidad=request.POST['localidad'],
            ciudad=request.POST['ciudad'],
            pais=request.POST['pais']
        )
        ubi.save()
        messages.success(request, 'Ubicación registrada exitosamente.')
        return redirect('registrar_contacto') 

    return render(request, "NewApp/registros/registrar_ubicacion.html")

def registrar_contacto(request):
    if request.method == 'POST':
        tel = request.POST.get('Tel', '')
        email = request.POST.get('email', '')
        tel_alternativo = request.POST.get('Tel_alternativo', '')

        print(f"Tel: {tel}, Email: {email}, Tel_alternativo: {tel_alternativo}")
        try:
            cont = Contacto(
                Tel=tel,
                email=email,
                Tel_alternativo=tel_alternativo
            )
            cont.save()
            messages.success(request, 'Contacto registrado exitosamente.')
            print("Redirigiendo a la página de fin...")
            return redirect("fin")  
        except ValueError as e:
            messages.error(request, f"Error al guardar el contacto: {e}")
            return render(request, "NewApp/registros/registrar_contacto.html")

    return render(request, "NewApp/registros/registrar_contacto.html")

def fin(request):
    return render(request, "NewApp/registros/fin.html")

# def form_con_api(request):
#     if request.method == "POST":
#         mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
#         # print(miFormulario)
#         if mi_formulario.is_valid():
#             informacion = mi_formulario.cleaned_data
            
#             curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
#             curso.save()

#             return render(request, "AppCoder/index.html")
#     else:
#         mi_formulario = CursoFormulario()

#     return render(request, "AppCoder/form_con_api.html", {"mi_formulario": mi_formulario})
