from urllib import response, request
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Hortelano, Huerta, Canteros


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def listadoHortelano(request):
    
    listadoHortelano = Hortelano.objects.filter(usuario=request.user)
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
    usuario = User.objects.get(username=request.POST['txtUsuario'])
    
    hortelano = Hortelano.objects.create(
        apodo= apodo, nombre = nombre, mail = mail, usuario = usuario
    )
    messages.success(request,"¡Hortelano Creado!")
    return redirect('/listadoHortelano')

def eliminarHortelano(request,id):
    hortelano = Hortelano.objects.get(id=id)
    hortelano.delete()
    return redirect('/listadoHortelano')
    
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
    return redirect('/listadoHortelano')


@login_required
def huertas_listar(request):
    hortelano = Hortelano.objects.get(usuario=request.user)
    listadoHuertas = Huerta.objects.filter(hortelano=hortelano)
    messages.success(request,"¡Huertas Listadas!")
    contexto =[
        { "listadoHuertas": listadoHuertas }
    ]
    return render(request, "huertas_listar.html",  { "listadoHuertas": listadoHuertas, "hortelano":hortelano, })

def huerta_editar(request,id):
     huerta = Huerta.objects.get(id=id)
     return render(request, "huerta_editar.html",{"huerta":huerta})

def huerta_modificar(request):
    id =request.POST['txtId']
    nombre = request.POST['txtNombre']
    coord_x = float(request.POST['txtCoordX'].replace('.','').replace(',','.'))
    coord_y =float(request.POST['txtCoordY'].replace('.','').replace(',','.'))
    ancho = float(request.POST['txtAncho'].replace('.','').replace(',','.'))
    largo = float(request.POST['txtLargo'].replace('.','').replace(',','.'))
    huerta = Huerta.objects.get(id=id)
    huerta.nombre= nombre
    huerta.coord_x= coord_x
    huerta.coord_y  = coord_y
    huerta.ancho= ancho
    huerta.largo= largo

    huerta.save()
    return redirect('/huertas_listar')


def huerta_eliminar(request,id):
    huerta = Huerta.objects.get(id=id)
    huerta.delete()
    return redirect('/huertas_listar')

def huerta_registrar(request):
    hortelano = Hortelano.objects.get(id=request.POST['txtHortelanoId'])
    nombre = request.POST['txtHuertaNombre']
    coord_x = float(request.POST['txtCoordX'].replace('.','').replace(',','.'))
    coord_y =float(request.POST['txtCoordY'].replace('.','').replace(',','.'))
    ancho = float(request.POST['txtAncho'].replace('.','').replace(',','.'))
    largo = float(request.POST['txtLargo'].replace('.','').replace(',','.'))
    
    
    huerta = Huerta.objects.create(
        hortelano= hortelano, nombre = nombre, coord_x = coord_x, coord_y = coord_y, ancho = ancho, largo = largo
    )
    messages.success(request,"¡Huerta Creada!")
    return redirect('/huertas_listar')

def huerta_mostrar(request, id):
    huerta = Huerta.objects.get(id=id)
    try:
        canteros = Canteros.objects.filter(huerta= huerta)
    except Canteros.DoesNotExist:
        canteros=""
    return render(request, "huerta_mostrar.html",{"huerta":huerta,"listadoCanteros":canteros})


def cantero_editar(request,id):
     cantero = Canteros.objects.get(id=id)
     return render(request, "cantero_editar.html",{"cantero":cantero})

def cantero_modificar(request):
    id =request.POST['txtId']
    nombre = request.POST['txtNombre']
    ubicacion_x = float(request.POST['txtUbicacionX'].replace('.','').replace(',','.'))
    ubicacion_y =float(request.POST['txtUbicacionY'].replace('.','').replace(',','.'))
    ancho = float(request.POST['txtAncho'].replace('.','').replace(',','.'))
    largo = float(request.POST['txtLargo'].replace('.','').replace(',','.'))
    cantero = Canteros.objects.get(id=id)
    cantero.nombre= nombre
    cantero.ubicacion_x= ubicacion_x
    cantero.ubicacion_y  = ubicacion_y
    cantero.ancho= ancho
    cantero.largo= largo
    cantero.save()
    return redirect('/configuracion/huerta_mostrar/'+str(cantero.huerta.id)+"/")


def cantero_eliminar(request,id):
    cantero = Canteros.objects.get(id=id)
    cantero.delete()
    return redirect('/configuracion/huerta_mostrar/'+str(cantero.huerta.id)+"/")

def cantero_registrar(request):
    huerta = Huerta.objects.get(id=request.POST['txtHuertaId'])
    nombre = request.POST['txtCanteroNombre']
    ubicacion_x = float(request.POST['txtUbicacionX'].replace('.','').replace(',','.'))
    ubicacion_y =float(request.POST['txtUbicacionY'].replace('.','').replace(',','.'))
    ancho = float(request.POST['txtAncho'].replace('.','').replace(',','.'))
    largo = float(request.POST['txtLargo'].replace('.','').replace(',','.'))
    cantero = Canteros.objects.create(
        huerta= huerta, nombre = nombre, ubicacion_x = ubicacion_x, ubicacion_y = ubicacion_y, ancho = ancho, largo = largo
    )
    messages.success(request,"Cantero Creado!")
    return redirect('/configuracion/huerta_mostrar/'+str(huerta.id)+"/")
