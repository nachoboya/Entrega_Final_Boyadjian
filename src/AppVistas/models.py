from django.db import models

# Create your models here.

class Producto(models.Model):

    modelo = models.CharField(max_length=40)
    articulo = models.IntegerField()
    stock = models.BooleanField()
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.modelo} - {self.articulo} - {self.stock} - {self.fecha} - {self.hora} - {self.usuario}"

class Proveedores(models.Model):
    razon = models.CharField(max_length=30)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.razon} - {self.email} - {self.ubicacion}"

class Marcas(models.Model):
    nombre = models.CharField(max_length=30)
    nacionalidad = models.CharField(max_length=30)
    Inicio_Actividad = models.DateField()
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.nombre} - {self.nacionalidad} - {self.Inicio_Actividad} - {self.fecha} - {self.hora} - {self.usuario}"