from django.contrib import admin
from AppVistas.models import Producto, Proveedores, Marcas

# Register your models here.

admin.site.register(Producto)
admin.site.register(Proveedores)
admin.site.register(Marcas)