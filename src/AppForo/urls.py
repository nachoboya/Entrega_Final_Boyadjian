from unicodedata import name
from django.urls import path
from AppForo.views import *



urlpatterns = [
    path("", foro, name='foro'),
    path("borrar/<id_mensaje>", borrar_mensaje, name="borrar_mensaje"),
    path("editar/<id_mensaje>", editar_mensaje, name="editar_mensaje"),
]
