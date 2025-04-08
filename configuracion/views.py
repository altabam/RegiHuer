
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.core import serializers



from .models import Cultivos, Hortelano,  Tierras_Cultivo, Enfermedades, Plagas, GaleriaImagen
from .forms import  CultivosForm, Tierras_CultivoForm, EnfermedadesForm, PlagasForm,GaleriaImagenForm
from accesibilidad.views import generarMenu

import json
# Create your views here.


@login_required
def gestion_hortelanos(request):
    menu = generarMenu("hola")
    listadoHortelano = Hortelano.objects.filter(usuario=request.user)
    messages.success(request,"¡Hortelanos Listados!")
    contexto ={ 
        "listadoHortelano": listadoHortelano, 
        "menu": menu
    }
    
    return render(request, "configuracionHortelano.html",  contexto)


def consultaPersona(request, persona_id):
    return HttpResponse("Estas mirando la persona: %s." % persona_id )

def registrarHortelano(request):
    apodo =request.POST['txtApodo']
    usuario = User.objects.get(username=request.POST['txtUsuario'])
    
    hortelano = Hortelano.objects.create(
        apodo= apodo,  
        usuario = usuario
    )
    messages.success(request,"¡Hortelano Creado!")
    return redirect('/configuracion/gestion_hortelanos')

def hortelano_eliminar(request,id):
    hortelano = Hortelano.objects.get(id=id)
    hortelano.delete()
    return redirect('/configuracion/gestion_hortelanos')
    
def hortelano_editar(request,id):
     hortelano = Hortelano.objects.get(id=id)
     return render(request, "hortelano_editar.html",{"hortelano":hortelano})

def hortelano_modificar(request):
    id =request.POST['txtId']
    apodo =request.POST['txtApodo']
    hortelano = Hortelano.objects.get(id=id)
    hortelano.apodo= apodo
    hortelano.save()
    return redirect('/configuracion/gestion_hortelanos')


# Create your views here.
def gestion_cultivos(request):
    listadoCultivos = Cultivos.objects.all()
    messages.success(request,"¡Cultivos Listados!")
    menu = generarMenu("hola")

    contexto ={ "listadoCultivos": listadoCultivos,  
               "menu":menu,
    } 
    return render(request, "cultivos_listar.html",  contexto)


def cultivo_agregar(request):
    if request.method == 'POST':
        form= CultivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_cultivos')
    else:
        form =CultivosForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "cultivo_editar.html", contexto )

def cultivo_editar(request,id):
    culitvo = Cultivos.objects.get(id = id)
    if request.method == 'POST':
        form= CultivosForm(request.POST, request.FILES, instance=culitvo)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_cultivos')
    else:
            form = CultivosForm( instance=culitvo)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "cultivo_editar.html",contexto)


def cultivo_eliminar(request,id):
    cultivo = Cultivos.objects.get(id=id)
    cultivo.delete()
    listadoCultivos = Cultivos.objects.all()
    messages.success(request,"¡Huertas Listadas!")
    contexto ={ "listadoCultivos": listadoCultivos,  } 
    return redirect('/configuracion/gestion_cultivos', contexto)



def cultivo_buscar(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    cultivos = Cultivos.objects.filter(nombre__contains=q)
    # generamos la query
    print(cultivos  )
    cultivo_fields = (
        'id',
        'familia',
        'nombre',
        'nombre_cientifico',
        'descripcion',
        'variedad',
        'imagen'
    )




def gestion_tierras_cultivo(request):
    menu = generarMenu("hola")
    listadoTierrasCultivo = Tierras_Cultivo.objects.all()
    messages.success(request,"¡Cultivos Listados!")
    contexto ={ "listadoTierrasCultivo": listadoTierrasCultivo,  
                "menu": menu
    } 
    return render(request, "tierras_cultivo_listar.html",  contexto)


def tierras_cultivo_agregar(request):
    if request.method == 'POST':
        form= Tierras_CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_tierras_cultivo/')
    else:
        form =Tierras_CultivoForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "tierras_cultivo_editar.html", contexto )

def tierras_cultivo_editar(request,id):
    tierras_cultivo = Tierras_Cultivo.objects.get(id = id)
    if request.method == 'POST':
        form= Tierras_CultivoForm(request.POST, instance=tierras_cultivo)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_tierras_cultivo/')
    else:
            form = Tierras_CultivoForm( instance=tierras_cultivo)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "tierras_cultivo_editar.html",contexto)


def tierras_cultivo_eliminar(request,id):
    tierras_cultivo = Tierras_Cultivo.objects.get(id = id)
    tierras_cultivo.delete()
    listadoTierrasCultivo = Tierras_Cultivo.objects.all()
    messages.success(request,"¡Tierras de Cultivo Listadas!")
    contexto ={ "listadoCultivos": listadoTierrasCultivo,  
               } 
    return redirect('/configuracion/gestion_tierras_cultivo/',contexto)



def tierras_cultivo_buscar(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    tierras_cultivo = Tierras_Cultivo.objects.filter(nombre__contains=q)
    # generamos la query

    user_fields = (
        'desc_corta',
        'descripcion'
    )

    # to json!
    data = serializers.serialize('json', tierras_cultivo, fields=user_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json") 


def gestion_enfermedades(request):
    menu = generarMenu("hola")
    listadoEnfermedades = Enfermedades.objects.all()
    messages.success(request,"¡Enfermedades Listados!")
    contexto ={ "listadoEnfermedades": listadoEnfermedades,  
                "menu": menu,
    } 
    return render(request, "enfermedades_listar.html",  contexto)


def enfermedades_agregar(request):
    if request.method == 'POST':
        form= EnfermedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_enfermedades/')
    else:
        form =EnfermedadesForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "enfermedades_editar.html", contexto )

def enfermedades_editar(request,id):
    enfermedades = Enfermedades.objects.get(id = id)
    if request.method == 'POST':
        form= EnfermedadesForm(request.POST, instance=enfermedades)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_enfermedades/')
    else:
            form = EnfermedadesForm( instance=enfermedades)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "enfermedades_editar.html",contexto)


def enfermedades_eliminar(request,id):
    enfermedades = Enfermedades.objects.get(id = id)
    enfermedades.delete()
    listadoEnfermedades = Enfermedades.objects.all()
    messages.success(request,"Enfermedades Listadas!")
    contexto ={ "listadoEnfermedades": listadoEnfermedades,  } 
    return redirect('/configuracion/gestion_enfermedades/',contexto)



def enfermedades_buscar(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    enfermedades = Enfermedades.objects.filter(nombre__contains=q)
    # generamos la query

    user_fields = (
        'descripcion',
        'tratamiento'
    )

    # to json!
    data = serializers.serialize('json', enfermedades, fields=user_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json") 


def gestion_plagas(request):
    menu = generarMenu("hola")
    listadoPlagas = Plagas.objects.all()
    messages.success(request,"¡Plagas Listados!")
    contexto ={ "listadoPlagas": listadoPlagas,  
               "menu": menu,
    } 
    return render(request, "plagas_listar.html",  contexto)


def plagas_agregar(request):
    if request.method == 'POST':
        form= PlagasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_plagas/')
    else:
        form =PlagasForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "plagas_editar.html", contexto )

def plagas_editar(request,id):
    plagas = Plagas.objects.get(id = id)
    if request.method == 'POST':
        form= PlagasForm(request.POST, instance=plagas)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_plagas/')
    else:
            form = PlagasForm( instance=plagas)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "plagas_editar.html",contexto)


def plagas_eliminar(request,id):
    plagas = Plagas.objects.get(id = id)
    plagas.delete()
    listadoPlagas = Plagas.objects.all()
    messages.success(request,"PlagasListadas!")
    contexto ={ "listadoPlagas": listadoPlagas,  } 
    return redirect('/configuracion/plagas_listar', contexto)



def plagas_buscar(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    plagas = Plagas.objects.filter(nombre__contains=q)
    # generamos la query

    user_fields = (
        'descripcion',
        'tratamiento'
    )

    # to json!
    data = serializers.serialize('json', plagas, fields=user_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json") 


def gestion_img_galeria_principal(request):
    listadoGalerias = GaleriaImagen.objects.all()
    print("listadoGalerias",listadoGalerias)
    messages.success(request,"¡Galerias Listadas!")
    menu = generarMenu("hola")

    contexto ={ "listadoGalerias": listadoGalerias,  
               "menu": menu,
    } 

    return render(request, "gestion_galerias.html",  contexto)


def galeria_imagenes_agregar(request):
    if request.method == 'POST':
        form= GaleriaImagenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_img_galeria_principal')
    else:
        form =GaleriaImagenForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "galeria_imagenes_editar.html", contexto )

def galeria_imagenes_editar(request,id):
    galeria = GaleriaImagen.objects.get(id = id)
    if request.method == 'POST':
        form= GaleriaImagenForm(request.POST, instance=galeria)
        if form.is_valid():
            print("edito imagen", id, galeria.imagen.url)
            form.save()
            return redirect('/configuracion/gestion_img_galeria_principal')
    else:
            form = GaleriaImagenForm( instance=galeria)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "galeria_imagenes_editar.html",contexto)

def galeria_imagenes_eliminar(request):
    return gestion_img_galeria_principal(request)

