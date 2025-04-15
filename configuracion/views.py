
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.core import serializers

import csv


from .models import Cultivos, Hortelano,  Tierras_Cultivo, Enfermedades, Plagas, GaleriaImagen, Temperaturas_Cultivos, Luz_Necesaria_Cultivo, Riego_Cultivo
from .forms import  CultivosForm, Tierras_CultivoForm, EnfermedadesForm, PlagasForm,GaleriaImagenForm, TemperaturasForm, LuzForm, RiegoForm
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
    cultivo = Cultivos.objects.get(id = id)
    if request.method == 'POST':
        form= CultivosForm(request.POST, request.FILES, instance=cultivo)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_cultivos')
    else:
            form = CultivosForm( instance=cultivo)
    
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



def gestion_temperaturas(request):
    listadoTemperaturas = Temperaturas_Cultivos.objects.all()
    messages.success(request,"¡Cultivos Listados!")
    menu = generarMenu("hola")

    contexto ={ "listadoTemperaturas": listadoTemperaturas,  
               "menu":menu,
    } 
    return render(request, "temperaturas_listar.html",  contexto)


def temperaturas_agregar(request):
    if request.method == 'POST':
        form= TemperaturasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_temperaturas')
    else:
        form =TemperaturasForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "temperatura_editar.html", contexto )

def temperaturas_editar(request,id):
    temperatura = Temperaturas_Cultivos.objects.get(id = id)
    if request.method == 'POST':
        form= TemperaturasForm(request.POST, request.FILES, instance=temperatura)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_temperaturas')
    else:
            form = TemperaturasForm( instance=temperatura)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "temperatura_editar.html",contexto)


def temperaturas_eliminar(request,id):
    temperatura = Temperaturas_Cultivos.objects.get(id=id)
    temperatura.delete()
    listadoTemperaturas = Temperaturas_Cultivos.objects.all()
    messages.success(request,"¡Temperaturas Listadas!")
    contexto ={ "listadoTemperaturas": listadoTemperaturas,  } 
    return redirect('/configuracion/gestion_temperaturas', contexto)


def gestion_luz_cultivos(request):
    listado = Luz_Necesaria_Cultivo.objects.all()
    messages.success(request,"¡Luz Necesaria para cultivos Listadas!")
    menu = generarMenu("hola")

    contexto ={ "listado": listado,  
               "menu":menu,
    } 
    return render(request, "luz_cultivo_listar.html",  contexto)


def luz_cultivos_agregar(request):
    if request.method == 'POST':
        form= LuzForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_luz_cultivos')
    else:
        form =LuzForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "luz_cultivo_editar.html", contexto )

def luz_cultivos_editar(request,id):
    luz = Luz_Necesaria_Cultivo.objects.get(id = id)
    if request.method == 'POST':
        form= LuzForm(request.POST, request.FILES, instance=luz)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_luz_cultivos')
    else:
            form = TemperaturasForm( instance=luz)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "luz_cultivo_editar.html",contexto)


def luz_cultivos_eliminar(request,id):
    luz = Luz_Necesaria_Cultivo.objects.get(id=id)
    luz.delete()
    listado = Luz_Necesaria_Cultivo.objects.all()
    messages.success(request,"¡Luz necesaria para los cultivos. Listadas!")
    contexto ={ "listado": listado,  } 
    return redirect('/configuracion/gestion_luz_cultivos', contexto)


def gestion_riego_cultivos(request):
    listado = Riego_Cultivo.objects.all()
    messages.success(request,"¡Riego necesario para cultivos Listadas!")
    menu = generarMenu("hola")

    contexto ={ "listado": listado,  
               "menu":menu,
    } 
    return render(request, "riego_cultivo_listar.html",  contexto)


def riego_cultivos_agregar(request):
    if request.method == 'POST':
        form= RiegoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_riego_cultivos')
    else:
        form =RiegoForm()

    contexto ={ 
            "accion":"Agregar", 
            "form": form,
         } 
    return render(request, "riego_cultivo_editar.html", contexto )

def riego_cultivos_editar(request,id):
    riego = Riego_Cultivo.objects.get(id = id)
    if request.method == 'POST':
        form= RiegoForm(request.POST, request.FILES, instance=riego)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/gestion_luz_cultivos')
    else:
            form = RiegoForm( instance=riego)
    
    contexto ={ 
            "accion":"Editar", 
            "form": form,
         } 
    return render(request, "riego_cultivo_editar.html",contexto)


def riego_cultivos_eliminar(request,id):
    riego = Riego_Cultivo.objects.get(id=id)
    riego.delete()
    listado = Riego_Cultivo.objects.all()
    messages.success(request,"¡Luz necesaria para los Cultivos Listadas!")
    contexto ={ "listado": listado,  } 
    return redirect('/configuracion/gestion_riego_cultivos', contexto)


def configuracion_carga_inicial(request):
    listado = listadoCargaInicial()
    mensaje ="carga con exito"
    contexto ={  
        "mensaje":mensaje , 
        "menu": generarMenu(request.user),
        "listado": listado , 
    } 
    return render (request, "carga_inicial.html",contexto)


def carga_inicial_tierra_cultivo(request):
    template_name = "configuracion/migrations/suelos.csv"
    #Disciplinas.objects.all().delete()
    with open (template_name) as f:
        reader = csv.reader(f )
        for row in reader:
           print("row:",row)
           print("Suelo:", row[0])
           Tierras_Cultivo.objects.create( desc_corta= row[0], descripcion =row[1] )
    mensaje ="carga con exito"
    contexto ={  
        "mensaje":mensaje , 
        "menu": generarMenu(request.user),
        "listado": listadoCargaInicial()

    } 
    return render (request, "carga_inicial.html",contexto)


def listadoCargaInicial():
    listado = [
        {
            'urlAgregar':"configuracion:carga_inicial_tierra_cultivo",
            'urlEliminar':"configuracion:eliminar_todo_tierra_cultivo",
            'nombre': "Carga Tipos de Suelos",
        }
        ]
               
    return listado

def eliminar_todo_tierra_cultivo(request):
    Tierras_Cultivo.objects.all().delete()
    mensaje ="registrso borrados con exito"
    contexto ={  
        "mensaje":mensaje , 
        "menu": generarMenu(request.user),
        "listado": listadoCargaInicial()

    } 
    return render (request, "carga_inicial.html",contexto)
