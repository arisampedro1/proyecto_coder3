﻿# proyecto_coder3
Proyecto Django - Papelera Descartes

Este proyecto es una aplicación web creada con Django para gestionar el registro de empresas, ubicaciones y contactos para un proveedor de artículos de librería y descartables llamado "Papelera Descartes". La aplicación permite a los usuarios registrar información sobre empresas, ubicaciones y contactos, y proporciona una interfaz sencilla para interactuar con estos datos.

Estructura del Proyecto
Modelos: Define las estructuras de datos para Ubicacion, Contacto, Empresa, y Dueño.
Vistas: Gestiona la lógica de negocio y el flujo de datos entre modelos y plantillas.
Plantillas: HTML que define la estructura de las páginas web.
URLs: Define las rutas para acceder a las vistas.
Instalación:
Python 3.12.4
Django 4.2 (o versión compatible)
Pasos para la Instalación:
1) Clona el repositorio: https://github.com/arisampedro1/proyecto_coder3.git
   cd proyecto_coder3
2) crear entoro virtual pipenv
   pip install pipenv
   pipenv --python 3.12.4
   pipenv shell
3) pip install -r requirements.txt
4) python manage.py migrate
5) python manage.py createsuperuser
6) python manage.py runserver
7) Abre tu navegador web y navega a http://127.0.0.1:8000/.

Rutas Disponibles
Inicio: / - Página principal de la aplicación. Desde aca también se puede buscar empresas ya registradas.
Registrar Formulario: /registrar-formulario/ - Formulario para registrar información de un dueño.
Registrar Empresa: /registrar-empresa/ - Formulario para registrar una empresa.
Registrar Ubicación: /registrar-ubicacion/ - Formulario para registrar una ubicación.
Registrar Contacto: /registrar-contacto/ - Formulario para registrar un contacto.
Fin: /fin/ - Página de confirmación después del registro exitoso de un contacto.

