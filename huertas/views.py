from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.core import serializers

from .models import Cultivos, Hortelano, Huerta, Canteros, Cantero_Cultivos
from .forms import HuertaForm, CanteroForm, Cantero_CultivosForm 
from accesibilidad.views import generarMenu

import json

@login_required
def gestion_huertas(request):
    hortelano = Hortelano.objects.get(usuario=request.user)
    listadoHuertas = Huerta.objects.filter(hortelano=hortelano)
    menu = generarMenu("hola")

    messages.success(request,"¡Huertas Listadas!")
    contexto ={ "listadoHuertas": listadoHuertas, "hortelano":hortelano, 
               "menu":menu,
    } 
    return render(request, "huertas_listar.html",  contexto)

def likePost(request):
        if request.method == 'GET':
               huerta_id = request.GET['id']
               huerta = Huerta.objects.get(pk=huerta_id)
               likedpost = Hortelano.objects.get(pk=huerta.hortelano.id) #getting the liked posts
               return HttpResponse("Success!") # Sending an success response
        else:
               return HttpResponse("Request method is not a GET")

@login_required
def huerta_agregar(request, id):
    hortelano = Hortelano.objects.get(id=id)
    if request.method == 'POST':
        form= HuertaForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/huertas/gestion_huertas')
    else:
        form = HuertaForm( )

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
            "hortelano": hortelano
         } 
    return render(request, "huerta_editar.html", contexto )

def huerta_editar(request,id):
    huerta = Huerta.objects.get(id = id)
    if request.method == 'POST':
        form= HuertaForm(request.POST, instance=huerta)
        if form.is_valid():
            form.save()
            return redirect('/huertas/gestion_huertas')
    else:
            form = HuertaForm( instance=huerta)
    
    contexto ={ 
            "accion":"Modificar", 
            "form": form,
            "hortelano": huerta.hortelano,
         } 
    return render(request, "huerta_editar.html",contexto)



def huerta_eliminar(request,id):
    huerta = Huerta.objects.get(id=id)
    huerta.delete()
    return redirect('/huertas/gestion_huertas')

def huerta_canteros_mostrar(request, id):
    print("pasa por huerta canteros mostrar")
    huerta = Huerta.objects.get(id=id)
    try:
        canteros = Canteros.objects.filter(huerta= huerta)
    except Canteros.DoesNotExist:
        canteros=""
    contexto={
        "huerta":huerta,
        "listadoCanteros":canteros,
        "hortelano": huerta.hortelano,
       
        }
    return render(request, "huerta_canteros_mostrar.html",contexto)

def huerta_cultivos_mostrar(request, id):
    huerta = Huerta.objects.get(id=id)
    try:
        canteros = Canteros.objects.filter(huerta= huerta)
        listadoCultivos = Cantero_Cultivos.objects.filter(cantero__in = canteros).distinct('cultivo_id')
    except Canteros.DoesNotExist:
        canteros=""
    contexto={
        "huerta":huerta,
        "listadoCultivos":listadoCultivos,
        "hortelano": huerta.hortelano,
       
        }
    return render(request, "huerta_cultivos_mostrar.html",contexto)

def huerta_cultivos_agregar(request, id):
    huerta = Huerta.objects.get(id=id)
    if request.method == 'POST':
        form= Cantero_CultivosForm(request.POST )
        if form.is_valid():
            form.save()
            return redirect('/huertas/huerta_cultivos_mostrar/'+str(huerta.id)+'/')
    else:
        form = Cantero_CultivosForm( )

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
            "hortelano": huerta.hortelano,
            "huerta": huerta,
         } 
    return render(request, "huerta_cultivos_editar.html", contexto )

def cantero_mostrar(request, id):
    cantero = Canteros.objects.get(id=id)
    huerta = Huerta.objects.get(id=cantero.huerta.id)
    try:
        cantero_cultivos = Cantero_Cultivos.objects.filter(cantero= cantero)
    except Canteros.DoesNotExist:
        cantero=""
    contexto={
        "huerta":huerta,
        "cantero": cantero,
        "listadoCanteroCultivos":cantero_cultivos,
        "hortelano": huerta.hortelano,
       
        }
    return render(request, "cantero_mostrar.html",contexto)


def cantero_editar(request,id):

     cantero = Canteros.objects.get(id=id)
     return render(request, "cantero_editar.html",{"cantero":cantero})


def cantero_agregar(request, id):
    huerta = Huerta.objects.get(id=id)
    if request.method == 'POST':
        form= CanteroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/huertas/huerta_canteros_mostrar/'+str(huerta.id)+'/')
    else:
        form = CanteroForm(initial= {'huerta': huerta})

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
            "hortelano": huerta.hortelano,
            "huerta": huerta,
         } 
    return render(request, "cantero_editar.html", contexto )

def cantero_editar(request,id):
    cantero = Canteros.objects.get(id = id)
    if request.method == 'POST':
        form= CanteroForm(request.POST, instance=cantero)
        if form.is_valid():
            form.save()
            return redirect('/huertas/huerta_canteros_mostrar/'+str(cantero.huerta.id)+'/')
    else:
            form = CanteroForm( instance=cantero)
    
    contexto ={ 
            "accion":"Modificar", 
            "form": form,
            "hortelano": cantero.huerta.hortelano,
            "huerta": cantero.huerta,

         } 
    return render(request, "cantero_editar.html",contexto)



def cantero_eliminar(request,id):
    cantero = Canteros.objects.get(id=id)
    cantero.delete()
    return redirect('/huertas/huerta_canteros_mostrar/'+str(cantero.huerta.id)+"/")

    
def canteros_listar(request):
    
    if request.method =='POST':
        # definimos el termino de busqueda
        data = json.load(request)
        q = data.get('id')
        #verificamos si el termino de busqueda es un documento de identidad
        canteros = list(Canteros.objects.filter(huerta =q).values())
        return JsonResponse({'context': canteros})
    else:
        return HttpResponseBadRequest()


def cantero_cultivos_editar(request,id):

     cantero_cultivos = Cantero_Cultivos.objects.get(id=id)
     return render(request, "cantero_cultivos_editar.html",{"cantero_cultivos":cantero_cultivos})


def cantero_cultivos_agregar(request, id):
    cantero = Canteros.objects.get(id=id)
    if request.method == 'POST':
        form= Cantero_CultivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/huertas/cantero_mostrar/'+str(cantero.id)+'/')
    else:
        form = Cantero_CultivosForm(initial= {'cantero': cantero})

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
            "cantero": cantero,
            "huerta": cantero.huerta,
            "hortelano": cantero.huerta.hortelano,
         } 
    return render(request, "cantero_cultivos_editar.html", contexto )

def cantero_cultivos_editar(request,id):
    cantero_cultivos = Cantero_Cultivos.objects.get(id = id)
    if request.method == 'POST':
        form= Cantero_CultivosForm(request.POST, instance=cantero_cultivos)
        if form.is_valid():
            form.save()
            return redirect('/huertas/cantero_mostrar/'+str(cantero_cultivos.cantero.id)+'/')
    else:
            form = Cantero_CultivosForm( instance=cantero_cultivos)
    
    contexto ={ 
            "accion":"Modificar", 
            "form": form,
            "hortelano": cantero_cultivos.cantero.huerta.hortelano,
            "huerta": cantero_cultivos.cantero.huerta,

         } 
    return render(request, "cantero_cultivos_editar.html",contexto)



def cantero_cultivos_eliminar(request,id):
    cantero = Canteros.objects.get(id=id)
    cantero.delete()
    return redirect('/huertas/huerta_canteros_mostrar/'+str(cantero.huerta.id)+"/")

def cantero_cultivos_mostrar(request, id):
    cantero = Canteros.objects.get(id=id)
    try:
        cantero_cultivos = Cantero_Cultivos.objects.filter(cantero= cantero)
    except Canteros.DoesNotExist:
        canteros=""
    contexto={
        "cantero":cantero,
        "huerta":cantero.huerta,
        "hortelano": cantero.huerta.hortelano,
        "listadoCanteroCultivos":cantero_cultivos,
       
        }
    return render(request, "cantero_cultivos_mostrar.html",contexto)

