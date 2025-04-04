
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.core import serializers



from .models import Cultivos, Hortelano, Huerta, Canteros, Cantero_Cultivos, Tierras_Cultivo, Enfermedades, Plagas, GaleriaImagen
from .forms import HuertaForm, CanteroForm, CultivosForm, Cantero_CultivosForm, Tierras_CultivoForm, EnfermedadesForm, PlagasForm,GaleriaImagenForm

import json
# Create your views here.


#@login_required
def gestion_hortelanos(request):
    listadoHortelano = Hortelano.objects.filter(usuario=request.user)
    messages.success(request,"¡Hortelanos Listados!")
    contexto ={ 
        "listadoHortelano": listadoHortelano, 
    }
    
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
    return redirect('/gestionHortelano')

def eliminarHortelano(request,id):
    hortelano = Hortelano.objects.get(id=id)
    hortelano.delete()
    return redirect('/gestionHortelano')
    
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
    return redirect('/gestionHortelano')


@login_required
def gestion_huertas(request):
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
            return redirect('configuracion/gestion_huertas')
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
            return redirect('configuracion/gestion_huertas')
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
    return redirect('configuracion/gestion_huertas')

def huerta_canteros_mostrar(request, id):
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
            return redirect('/configuracion/huerta_cultivos_mostrar/'+str(huerta.id)+'/')
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
            return redirect('/configuracion/huerta_canteros_mostrar/'+str(huerta.id)+'/')
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
            return redirect('/configuracion/huerta_canteros_mostrar/'+str(cantero.huerta.id)+'/')
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
    return redirect('/configuracion/huerta_canteros_mostrar/'+str(cantero.huerta.id)+"/")

def gestion_cultivos(request):
    listadoCultivos = Cultivos.objects.all()
    print("paso por aqui")
    messages.success(request,"¡Cultivos Listados!")
    contexto ={ "listadoCultivos": listadoCultivos,  } 
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

def cantero_cultivos_editar(request,id):

     cantero_cultivos = Cantero_Cultivos.objects.get(id=id)
     return render(request, "cantero_cultivos_editar.html",{"cantero_cultivos":cantero_cultivos})


def cantero_cultivos_agregar(request, id):
    cantero = Canteros.objects.get(id=id)
    if request.method == 'POST':
        form= Cantero_CultivosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/configuracion/cantero_mostrar/'+str(cantero.id)+'/')
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
            return redirect('/configuracion/cantero_mostrar/'+str(cantero_cultivos.cantero.id)+'/')
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
    return redirect('/configuracion/huerta_canteros_mostrar/'+str(cantero.huerta.id)+"/")

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


def gestion_img_galeria_principal(request):
    listadoGalerias = GaleriaImagen.objects.all()
    print("listadoGalerias",listadoGalerias)
    messages.success(request,"¡Galerias Listadas!")
    contexto ={ "listadoGalerias": listadoGalerias,  } 
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

