from contextlib import ContextDecorator
from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseBadRequest, HttpResponse, HttpRequest
from django.core import serializers


from django.http import HttpResponseRedirect
from django.views.generic import CreateView


from .models import Cultivos, Hortelano, Huerta, Canteros, Cantero_Cultivos, Tierras_Cultivo, Enfermedades, Plagas
from .forms import HuertaForm, CanteroForm, CultivosForm, Cantero_CultivosForm, Tierras_CultivoForm, EnfermedadesForm, PlagasForm


# Create your views here.


@login_required
def listadoHortelano(request):
    
    listadoHortelano = Hortelano.objects.filter(usuario=request.user)
    messages.success(request,"¡Hortelanos Listados!")
    contexto =[
        { "listadoHortelano": listadoHortelano }
    ]
    return render(request, "configuracionHortelano.html",  contexto)


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
    contexto ={ "listadoHuertas": listadoHuertas, "hortelano":hortelano, } 
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
            return redirect('/huertas_listar')
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
            return redirect('/huertas_listar')
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
    return redirect('/huertas_listar')

def huerta_mostrar(request, id):
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
    return render(request, "huerta_mostrar.html",contexto)

def cantero_mostrar(request, id):
    cantero_cultivos = Cantero_Cultivos.objects.get(id=id)
    try:
        canteros = Canteros.objects.filter(huerta= huerta)
    except Canteros.DoesNotExist:
        canteros=""
    contexto={
        "huerta":huerta,
        "listadoCanteros":canteros,
        "hortelano": huerta.hortelano,
       
        }
    return render(request, "huerta_mostrar.html",contexto)


def cantero_editar(request,id):

     cantero = Canteros.objects.get(id=id)
     return render(request, "cantero_editar.html",{"cantero":cantero})


def cantero_agregar(request, id):
    huerta = Huerta.objects.get(id=id)
    if request.method == 'POST':
        form= CanteroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/huerta_mostrar/'+str(huerta.id)+'/')
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
            return redirect('/configuracion/huerta_mostrar/'+str(cantero.huerta.id)+'/')
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
    return redirect('/configuracion/huerta_mostrar/'+str(cantero.huerta.id)+"/")

def cultivos_listar(request):
    listadoCultivos = Cultivos.objects.all()
    messages.success(request,"¡Cultivos Listados!")
    contexto ={ "listadoCultivos": listadoCultivos,  } 
    return render(request, "cultivos_listar.html",  contexto)


def cultivo_agregar(request):
    if request.method == 'POST':
        form= CultivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cultivos_listar/')
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
            return redirect('/cultivos_listar/')
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
    return redirect('/cultivos_listar/', contexto)



def cultivo_buscar(request):

    # si no es una peticion ajax, devolvemos error 400
    if not request.is_ajax() or request.method != "POST":
        return HttpResponseBadRequest()

    # definimos el termino de busqueda
    q = request.POST['q']

    #verificamos si el termino de busqueda es un documento de identidad
    cultivos = Cultivos.objects.filter(nombre__contains=q)
    # generamos la query

    user_fields = (
        'nombre',
        'especie',
        'descripcion'
    )

    # to json!
    data = serializers.serialize('json', cultivos, fields=user_fields)

    # eso es todo por hoy ^^
    return HttpResponse(data, content_type="application/json")    


def tierras_cultivo_listar(request):
    listadoTierrasCultivo = Tierras_Cultivo.objects.all()
    messages.success(request,"¡Cultivos Listados!")
    contexto ={ "listadoTierrasCultivo": listadoTierrasCultivo,  } 
    return render(request, "tierras_cultivo_listar.html",  contexto)


def tierras_cultivo_agregar(request):
    if request.method == 'POST':
        form= Tierras_CultivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/tierras_cultivo_listar/')
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
            return redirect('/tierras_cultivo_listar/')
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
    contexto ={ "listadoCultivos": listadoTierrasCultivo,  } 
    return redirect('/tierras_cultivo_listar/', contexto)



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


def enfermedades_listar(request):
    listadoEnfermedades = Enfermedades.objects.all()
    messages.success(request,"¡Enfermedades Listados!")
    contexto ={ "listadoEnfermedades": listadoEnfermedades,  } 
    return render(request, "enfermedades_listar.html",  contexto)


def enfermedades_agregar(request):
    if request.method == 'POST':
        form= EnfermedadesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/enfermedades_listar/')
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
            return redirect('/enfermedades_listar/')
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
    return redirect('/enfermedades_listar/', contexto)



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


def plagas_listar(request):
    listadoPlagas = Plagas.objects.all()
    messages.success(request,"¡Plagas Listados!")
    contexto ={ "listadoPlagas": listadoPlagas,  } 
    return render(request, "plagas_listar.html",  contexto)


def plagas_agregar(request):
    if request.method == 'POST':
        form= PlagasForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/plagas_listar/')
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
            return redirect('/plagas_listar/')
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
    return redirect('/plagas_listar/', contexto)



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