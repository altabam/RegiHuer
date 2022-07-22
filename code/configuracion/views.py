from urllib import response, request
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect, render
from .models import Hortelano
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages


def index(request):
    listadoHortelano = Hortelano.objects.all()
    messages.success(request,"¡Hortelanos Listados!")
    contexto =[
        { "listadoHortelano": listadoHortelano }
    ]
    return render(request, "configuracionHortelano.html",  { "listadoHortelano": listadoHortelano })

def consultaPersona(request, persona_id):
    return HttpResponse("Estas mirando la persona: %s." % persona_id )

def registrarHortelano(request):
    apodo =request.POST['txtApodo']
    nombre = request.POST['txtNombre']
    mail = request.POST['txtMail']
    hortelano = Hortelano.objects.create(
        apodo= apodo, nombre = nombre, mail = mail
    )
    messages.success(request,"¡Hortelano Creado!")
    return redirect('/configuracion')

def eliminarHortelano(request,id):
    hortelano = Hortelano.objects.get(id=id)
    hortelano.delete()
    return redirect('/configuracion')
    
def editarHortelano(request,id):
     hortelano = Hortelano.objects.get(id=id)
     return render(request, "editarHortelano.html",{"hortelano":hortelano})

def modificarHortelano(request):
    id =request.POST['txtId']
    apodo =request.POST['txtApodo']
    nombre = request.POST['txtNombre']
    mail = request.POST['txtMail']
    hortelano = Hortelano.objects.get(id=id)
    hortelano.apodo= apodo
    hortelano.nombre = nombre 
    hortelano.mail = mail
    hortelano.save()
    return redirect('/configuracion')
