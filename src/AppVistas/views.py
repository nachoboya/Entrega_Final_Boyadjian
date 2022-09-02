from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppVistas.models import Producto, Proveedores, Marcas
from AppVistas.forms import ProductoFormulario, MarcaFormulario
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#Permisos de usuario
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def vistas(request):

    return render(request, "AppVistas/vistas.html")

def productos(request):

    productos = Producto.objects.all()

    if request.method == "GET":
        form_producto = ProductoFormulario()
        
        contexto_pro = {
        "mensaje_pro1":"Nuestros productos",
        "mensaje_pro2":"Este es el listado de nuestros productos",
        "productos":productos,
        "form_producto":form_producto
        }

        return render(request, "AppVistas/productos.html", contexto_pro)

    else:
        
        form_producto = ProductoFormulario(request.POST)

        if form_producto.is_valid():

            data = form_producto.cleaned_data

            modelo = data.get("modelo")
            articulo = data.get("articulo")
            stock = data.get("stock")
            producto = Producto(modelo=modelo, articulo=articulo, stock=stock)

            producto.save()

            form_producto = ProductoFormulario()

            contexto_pro = {
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Nuevo producto cargado!",
            "productos":productos,
            "form_producto":form_producto
            }

            return render(request, "AppVistas/productos.html", contexto_pro)
        else:
            return render(request, "AppVistas/volver.html")

def borrar_producto(request, id_producto):

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
        "form_producto":form_producto
        }

        return render(request, "AppVistas/productos.html",contexto_pro)

def formulario_busqueda(request):
    return render(request, "AppVistas/formulario_busqueda.html")

def buscar(request):

    producto_modelo = request.GET.get("producto", None)

    if not producto_modelo or not Producto.objects.filter(modelo__icontains=producto_modelo):
        return render(request, "AppVistas/volver.html")

    producto_lista = Producto.objects.filter(modelo__icontains=producto_modelo)
    return render(request, "AppVistas/resultado_busqueda.html", {"productos": producto_lista})

def actualizar_producto(request,id_producto):

    if request.method == "GET":
        formulario = ProductoFormulario()
        contexto={
            "mensaje_pro1":"Nuestros productos",
            "mensaje_pro2":"Este es el listado de nuestros productos",
            "formulario":formulario,
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
                return redirect("inicio")

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

    marcas = Marcas.objects.all()
    if request.method == "GET":
        form_marca = MarcaFormulario()

        contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Trabajamos únicamente con las mejores marcas del mercado",
            "marcas":marcas,
            "form_marca":form_marca
        }

        return render(request, "AppVistas/marcas.html", contexto_mar)
    else:

        form_marca = MarcaFormulario(request.POST)

        if form_marca.is_valid():

            data = form_marca.cleaned_data

            nombre = data.get("nombre")
            nacionalidad = data.get("nacionalidad")
            marca = Marcas(nombre=nombre, nacionalidad=nacionalidad)

            marca.save()

            form_marca = MarcaFormulario()
            contexto_mar = {
            "mensaje_mar1":"Las marcas",
            "mensaje_mar2":"Nueva marca cargada!",
            "marcas":marcas,
            "form_marca":form_marca
            }
            return render(request, "AppVistas/marcas.html", contexto_mar)
        else:
            return render(request, "AppVistas/volver.html")

def borrar_marca(request, id_marca):

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
        "form_marca":form_marca
        }

        return render(request, "AppVistas/marcas.html",contexto_mar)