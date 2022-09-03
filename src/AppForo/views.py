from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppForo.models import Foro
from AppForo.forms import ForoFormulario
from datetime import datetime

# Create your views here.

def foro(request):

    mensajes = Foro.objects.all()

    if request.method == "GET":
        form_foro = ForoFormulario()
        
        contexto = {
        "mensajes":mensajes,
        "form_foro":form_foro
        }

        return render(request, "AppForo/foro.html", contexto)

    else:
        
        form_foro = ForoFormulario(request.POST)

        if form_foro.is_valid():

            data = form_foro.cleaned_data

            chat = data.get("chat")
            fecha = datetime.now()
            hora = datetime.now().strftime('%H:%M:%S')
            usuario = request.user
            mensaje = Foro(chat=chat, fecha=fecha,hora=hora, usuario=usuario)
            
            mensaje.save()

            form_foro = ForoFormulario()

            contexto = {
            "mensajes":mensajes,
            "form_foro":form_foro
            }

            return render(request, "AppForo/foro.html", contexto)
        else:
            return render(request, "AppVistas/volver.html")

def borrar_mensaje(request, id_mensaje):

    mensajes = Foro.objects.all()
    form_foro = ForoFormulario()

    try:
        mensaje = Foro.objects.get(id=id_mensaje)
        mensaje.delete()

        return redirect("foro")
    except:
        return render(request, "AppVistas/volver.html")

def editar_mensaje(request,id_mensaje):

    if request.method == "GET":
        form_foro = ForoFormulario()
        contexto={
            "form_foro":form_foro,
        }
        return render(request, "AppForo/editar_mensaje.html", contexto)
    else:
        form_foro = ForoFormulario(request.POST)

        if form_foro.is_valid():
            data = form_foro.cleaned_data

            try:
                mensaje = Foro.objects.get(id=id_mensaje)

                mensaje.chat = data.get("chat")
                
                mensaje.save()
            except:
                return render(request, "AppVistas/volver.html")

        return redirect("foro")