from unicodedata import name
from django.urls import path
from AppExpo.views import *

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("inicio/", inicio, name='inicio'),

    path("", iniciar_sesion, name='iniciar_sesion'),
    path("register/",registrar_usuario, name='registro'),
    path("logout/", LogoutView.as_view(template_name="AppExpo/logout.html"), name="logout"),
    path("edit/", editar_usuario, name="editar_usuario"),
    path("avatar/", agregar_avatar, name="agregar_avatar"),

    path("about/", about, name="about"),    
]