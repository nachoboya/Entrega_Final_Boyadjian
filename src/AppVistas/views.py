from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppVistas.models import Producto, Proveedores, Marcas
from AppVistas.forms import ProductoFormulario, MarcaFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from AppExpo.models import Avatar

from datetime import datetime

#Permisos de usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def vistas(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    return render(request, "AppVistas/vistas.html", {"imagen":avatar.imagen.url})

def productos(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    productos = Producto.objects.all()

    if request.method == "GET":
        form_producto = ProductoFormulario()
        
        contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Este es el listado de nuestros productos",
        "productos":productos,
        "form_producto":form_producto,
        "imagen":avatar.imagen.url
        }

        return render(request, "AppVistas/productos.html", contexto_pro)

    else:
        
        form_producto = ProductoFormulario(request.POST)

        if form_producto.is_valid():

            data = form_producto.cleaned_data

            modelo = data.get("modelo")
            articulo = data.get("articulo")
            stock = data.get("stock")
            fecha = datetime.now()
            hora = datetime.now().strftime('%H:%M:%S')
            usuario = request.user
            producto = Producto(modelo=modelo, articulo=articulo, stock=stock, fecha=fecha, hora=hora, usuario=usuario)

            producto.save()

            form_producto = ProductoFormulario()

            contexto_pro = {
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Nuevo producto cargado!",
            "productos":productos,
            "form_producto":form_producto,
            "imagen":avatar.imagen.url
            }

            return render(request, "AppVistas/productos.html", contexto_pro)
        else:
            return render(request, "AppVistas/volver.html", {"imagen":avatar.imagen.url})

def borrar_producto(request, id_producto):
    
    avatar = Avatar.objects.filter(usuario=request.user).first()
    productos = Producto.objects.all()
    form_producto = ProductoFormulario()

    try:
        producto = Producto.objects.get(id=id_producto)
        producto.delete()

        return redirect("productos")
    except:
        contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Error, no se puede borrar el producto!",
        "productos":productos,
        "form_producto":form_producto,
        "imagen":avatar.imagen.url
        }

        return render(request, "AppVistas/productos.html",contexto_pro)

def detalle_producto(request, id_producto):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    productos = Producto.objects.get(id=id_producto)

    contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Este es el detalle:",
        "productos":productos,
        "imagen":avatar.imagen.url
        }

    return render(request, "AppVistas/producto_detalle.html",contexto_pro)

def formulario_busqueda(request):
        
    avatar = Avatar.objects.filter(usuario=request.user).first()

    return render(request, "AppVistas/formulario_busqueda.html", {"imagen":avatar.imagen.url})

def buscar(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    producto_modelo = request.GET.get("producto", None)

    if not producto_modelo or not Producto.objects.filter(modelo__icontains=producto_modelo):
        return render(request, "AppVistas/volver.html", {"imagen":avatar.imagen.url})

    producto_lista = Producto.objects.filter(modelo__icontains=producto_modelo)
    return render(request, "AppVistas/resultado_busqueda.html", {"productos": producto_lista, "imagen":avatar.imagen.url})

def actualizar_producto(request,id_producto):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    if request.method == "GET":
        formulario = ProductoFormulario()
        contexto={
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Este es el listado de nuestros productos",
            "formulario":formulario,
            "imagen":avatar.imagen.url
        }
        return render(request, "AppVistas/producto_actualizar.html", contexto)
    else:
        formulario = ProductoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                producto = Producto.objects.get(id=id_producto)

                producto.modelo = data.get("modelo")
                producto.articulo = data.get("articulo")

                producto.save()
            except:
                return render(request, "AppVistas/volver.html", {"imagen":avatar.imagen.url})

        return redirect("productos")

class ProveedoresList(LoginRequiredMixin, ListView):

    model = Proveedores
    template_name = "AppVistas/proveedores_list.html"

class ProveedoresDetail(DetailView):

    model = Proveedores
    template_name = "AppVistas/proveedores_detail.html"

class ProveedoresCreate(CreateView):

    model = Proveedores
    success_url = "/vista/proveedores/"
    fields = ["razon", "email", "ubicacion"]

class ProveedoresUpdate(UpdateView):

    model = Proveedores
    success_url = "/vista/proveedores/"
    fields = ["razon", "email", "ubicacion"]

class ProveedoresDelete(DeleteView):

    model = Proveedores
    success_url = "/vista/proveedores/"

def marcas(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    marcas = Marcas.objects.all()
    if request.method == "GET":
        form_marca = MarcaFormulario()

        contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Trabajamos únicamente con las mejores marcas del mercado",
            "marcas":marcas,
            "form_marca":form_marca,
            "imagen":avatar.imagen.url
        }

        return render(request, "AppVistas/marcas.html", contexto_mar)
    else:

        form_marca = MarcaFormulario(request.POST)

        if form_marca.is_valid():

            data = form_marca.cleaned_data

            nombre = data.get("nombre")
            nacionalidad = data.get("nacionalidad")
            Inicio_Actividad = data.get("Inicio_Actividad")
            fecha = datetime.now()
            hora = datetime.now().strftime('%H:%M:%S')
            usuario = request.user
            marca = Marcas(nombre=nombre, nacionalidad=nacionalidad, Inicio_Actividad=Inicio_Actividad, fecha=fecha, hora=hora, usuario=usuario)

            marca.save()

            form_marca = MarcaFormulario()
            contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Nueva marca cargada!",
            "marcas":marcas,
            "form_marca":form_marca,
            "imagen":avatar.imagen.url
            }
            return render(request, "AppVistas/marcas.html", contexto_mar)
        else:
            return render(request, "AppVistas/volver.html", {"imagen":avatar.imagen.url})

def borrar_marca(request, id_marca):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    marcas = Marcas.objects.all()
    form_marca = MarcaFormulario()

    try:
        marca = Marcas.objects.get(id=id_marca)
        marca.delete()

        return redirect("marcas")
    except:
        contexto_mar = {
        "mensaje_mar1":"Nuestros marcas",
        "mensaje_mar2":"Error, no se puede borrar la marca!",
        "marcas":marcas,
        "form_marca":form_marca,
        "imagen":avatar.imagen.url
        }

        return render(request, "AppVistas/marcas.html",contexto_mar)

def detalle_marca(request, id_marca):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    marcas = Marcas.objects.get(id=id_marca)

    contexto_mar = {
        "mensaje_pro1":"Nuestras marcas",
        "mensaje_pro2":"Este es el detalle:",
        "marcas":marcas,
        "imagen":avatar.imagen.url
        }

    return render(request, "AppVistas/marca_detalle.html",contexto_mar)

def actualizar_marca(request,id_marca):

    avatar = Avatar.objects.filter(usuario=request.user).first()

    if request.method == "GET":
        formulario = MarcaFormulario()
        contexto={
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Este es el listado de nuestros productos",
            "formulario":formulario,
            "imagen":avatar.imagen.url
        }
        return render(request, "AppVistas/marca_actualizar.html", contexto)
    else:
        formulario = MarcaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            try:
                marca = Marcas.objects.get(id=id_marca)

                marca.nombre = data.get("nombre")
                marca.nacionalidad = data.get("nacionalidad")
                marca.Inicio_Actividad = data.get("Inicio_Actividad")

                marca.save()
            except:
                return render(request, "AppVistas/volver.html", {"imagen":avatar.imagen.url})

        return redirect("marcas")