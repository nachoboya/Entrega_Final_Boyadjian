from django.db import models

# Create your models here.

class Foro(models.Model):

    chat = models.CharField(max_length=400)
    fecha = models.DateField()
    hora = models.TimeField()
    usuario = models.CharField(max_length=400)

    def __str__(self):
        return f"{self.chat} - {self.fecha} - {self.hora} - {self.usuario}"