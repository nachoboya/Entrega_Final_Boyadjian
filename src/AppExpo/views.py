from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppExpo.models import Avatar
from AppExpo.forms import AvatarForm, UserEditForm

# Auth imports
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


from AppExpo.forms import UserCustomCreationForm

# Permisos de usuario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.


def inicio(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    try:
        contexto = {"imagen":avatar.imagen.url}
        
    except:
        contexto = {"imagen":""}

    return render(request, "AppExpo/index.html", contexto)


def iniciar_sesion(request):
    if request.method == "GET":
        formulario = AuthenticationForm()

        contexto = {
            "form": formulario
        }

        return render(request, "AppExpo/login.html", contexto)
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = authenticate(username=data.get(
                "username"), password=data.get("password"))

            if usuario is not None:
                login(request, usuario)
                avatar1 = Avatar.objects.filter(usuario=request.user).first()

                if avatar1 is not None:
                    return redirect("inicio")
                else:
                    return redirect("agregar_avatar")
                
            else:
                contexto = {
                    "error": "Credenciales no válidas",
                    "form": formulario
                }
                return render(request, "AppExpo/login.html", contexto)
        else:
            contexto = {
                "error": "Formulario no válido",
                "form": formulario
            }
            return render(request, "AppExpo/login.html", contexto)


def registrar_usuario(request):


    if request.method == "GET":
        formulario = UserCustomCreationForm()
        return render(request, "AppExpo/registro.html", {"form": formulario})

    else:
        formulario = UserCustomCreationForm(request.POST)

        if formulario.is_valid():
            formulario.save()

            return redirect("iniciar_sesion")
        else:
            return render(request, "AppExpo/registro.html", {"form": formulario, "error": "Formulario no válido"})


@login_required
def editar_usuario(request):

    avatar = Avatar.objects.filter(usuario=request.user).first()
    usuario = request.user

    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email,
                            "first_name": request.user.first_name, "last_name": request.user.last_name})
        try:
            contexto = {"form": form,"imagen":avatar.imagen.url}
            
        except:
            contexto = {"form": form,"imagen":""}
        return render(request, "AppExpo/update_user.html",contexto)
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()
            return redirect("inicio")
        try:
            contexto = {"form": form,"imagen":avatar.imagen.url}
        
        except:
            contexto = {"form": form,"imagen":""}
        
        return render(request, "AppExpo/update_user.html", contexto)


@login_required
def agregar_avatar(request):

    if request.method == "GET":
        form = AvatarForm()
        contexto = {"form": form}
        return render(request, "AppExpo/agregar_avatar.html", contexto)
    else:
        form = AvatarForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data

            usuario = User.objects.get(username=request.user)
            avatar = Avatar(usuario=usuario, imagen=data["imagen"])

            avatar.save()
        return redirect("inicio")



def about(request):
        
    avatar = Avatar.objects.filter(usuario=request.user).first()
    try:
        contexto = {"imagen":avatar.imagen.url}
        
    except:
        contexto = {"imagen":""}

    return render(request, "AppExpo/about.html", contexto)
