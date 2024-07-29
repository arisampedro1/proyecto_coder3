from django.db import models


class Empresa(models.Model):
    razon_social = models.CharField(max_length=200)
    cuil = models.IntegerField()
    nombre_de_fantasia = models.CharField(max_length=200)
    actividad_comercial = models.TextField()

    def __str__(self):
        return f"{self.nombre_de_fantasia} ({self.actividad_comercial})"

class Dueño(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Ubicacion(models.Model):
    direccion = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=200)
    pais = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.pais}"

class Contacto(models.Model):
    Tel = models.IntegerField()
    email = models.CharField(max_length=200)
    Tel_alternativo = models.IntegerField()

    def __str__(self):
        return f"{self.email}"
    


