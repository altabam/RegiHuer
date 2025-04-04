from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import hashlib, datetime, random, os
from .models import UsuarioPromesa
from .forms import RegistracionUsuarioForm, UsuarioPromesaForm
from configuracion.models import GaleriaImagen,Galeria
from accesibilidad.models import Menu
# Create your views here.

def generarTagPrincipalHoja(menu, orden):
    if orden > 1:
      menuTitle = 'menu-title_'+str(orden)
    else:
        menuTitle=''
    me =[]
    tag = [{'tag':'<li>'}]
    me = [tag]
    
    tag = []
    tag.append({'tag':'<a>','href':menu.url, 'class':'menu'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'<h2>', 'class':'menu-title '+menuTitle, 'descripcion':menu.nombre})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'<ul>', 'class':'menu-dropdown', })
    me.append(tag)

    tag =[]
    tag.append({'tag':'</ul>'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'</a>'})
    me.append(tag)
    
    tag =[]
    tag.append({'tag':'</li>'})
    me.append(tag)
  
    return me
def generarTagPrincipalPadre(menu,orden):
    if orden > 1:
      menuTitle = 'menu-title_'+str(orden)
    else:
        menuTitle=''
    me =[]
    tag = [{'tag':'<li>'}]
    me = [tag]
    
    tag = []
    tag.append({'tag':'<div>','class':'menu'})
    me.append(tag)
    tag =[]

    tag.append({'tag':'<h2>', 'class':'menu-title '+menuTitle, 'descripcion':menu.nombre})
    me.append(tag)
    tag =[]
    tag.append({'tag':'<ul>', 'class':'menu-dropdown', })
    me.append(tag)
    menuHijos = Menu.objects.filter(menuPadre = menu)
    print("menu hijo:", menuHijos)
    for mh in menuHijos:
        tag=[]
        if mh.tipo=='H':
            print('tag hijo mh:', mh)
            tag.append({'tag':'<li>'})
            me.append(tag)
 
            tag=[]
            tag.append({'tag':'<a>','href':mh.url, 'class':'menu', 'descripcion':mh.nombre})
            me.append(tag)
        
            tag =[]
            tag.append({'tag':'</a>'})
            me.append(tag)

            tag=[]
            tag.append({'tag':'</li>'})
            me.append(tag)
    tag =[]
    tag.append({'tag':'</ul>'})
    me.append(tag)
    tag =[]
    tag.append({'tag':'</div>'})
    me.append(tag)
    tag =[]
    tag.append({'tag':'</li>'})
    me.append(tag)
  

              #  <h2 class="menu-title menu-title_2nd">Otros</h2>
              #  <ul class="menu-dropdown">
#                  <li><a href="/configuracion/gestionar_img_galeria_principal">Galeria Imag</a></li>
 #                 <li>Jim</li>
  #                <li>Andy</li>
   #             </ul>
    #S          </div>


    return me
def generarMenu(user):
  menu =[]
  menues = Menu.objects.filter( menuPadre__isnull = True )
  orden = 1
  for me in menues:
      if me.tipo=="H":
          menu.extend(generarTagPrincipalHoja(me,orden))
      elif me.tipo == 'P':
          menu.extend(generarTagPrincipalPadre(me,orden))
      if orden == 4:
       orden =1
      else:
        orden +=1
      
  
  print(menues)
  #menu = ["<a href='/configuracion/cultivos_listar' class='menu'>"]

 # menu.append('<h2 class="menu-title">Cultivos</h2>')

 # menu.append('<ul class="menu-dropdown"></ul>')
 # menu.append('</a>"')
  print("menu generado:",menu)
  return menu

def index(request):
    contexto={}
    menu = generarMenu("hola")
    if Galeria.objects.filter(id=1).exists():
        galeria = Galeria.objects.get(id=1)
        galeriaImagen = GaleriaImagen.objects.filter(galeria= galeria)
        contexto = {'listadoGalerias': galeriaImagen,}

    contexto["menu"]=menu
    return render(request, "index.html", contexto)

def registrar(request):
    #up = UsuarioPromesa.objects.all().delete()
    if request.method=='POST':
        form = UsuarioPromesaForm(request.POST)
        print("no si es valido")
        if form.is_valid():
            usuarioPromesa = generarUsuarioPromesa(request,form)
            if(usuarioPromesa):
                username = form.cleaned_data['username']
                messages.success(request, f'Usuario {username} creado')
                enviarEmail(usuarioPromesa)
                return render(request, "index.html")
    else:
        form = UsuarioPromesaForm()
    contexto = {'form': form,}
    return render(request, "registration/registracion.html", contexto)

def enviarEmail(up):
    
    # Renderizar la plantilla
    url_app = "https://"+os.getenv("URL_APP")+ "/validacion?tk="+up.token
    print(url_app)
    print(up.fecha)
    un = up.username
    mensaje = render_to_string("registration/templateEmail.html",{'username':un, 'url_app':url_app})    # Enviar el correo
    print (mensaje)
    email = EmailMessage(
      subject='RegiHuer - Registro de Usuario',
      body=mensaje,
      from_email='altabam@gmail.com',
      to=[up.email],
    )
    
    email.content_subtype = 'html'  # Define el tipo como HTML
  #  email.send()
def generarUsuarioPromesa(request,form):
    bandera = True
    if(User.objects.filter(username=form.cleaned_data['username']).exists()):
      upun = User.objects.filter(username=form.cleaned_data['username']).first()
      messages.error(request, 'El nombre de usuario se encuentra registrado')
      bandera = False
    if(User.objects.filter(username=form.cleaned_data['email']).exists()):
      upem = User.objects.filter(email = form.cleaned_data['email']).first()
      messages.error(request, 'El email de usuario se encuentra registrado')
      bandera = False
    print("no se si paso por aca")
    
    if(bandera):
        form.save()
        up = UsuarioPromesa.objects.get(username = form.cleaned_data['username'])
        alea = str(random.random())
        text = up.first_name + alea + up.username +str(up.fecha) + up.email + str(up.pk) + up.last_name 
        print(text)
        up.token = hashlib.sha256(text.encode()).hexdigest()
        up.aleatorio = alea
        print(up.token)
        print(up.aleatorio)
        up.save()
        return up  
    else:
        return False

def mailValidador(request):
    if request.method=='GET':
        token = request.GET.get('tk')
        print (token)
        up = UsuarioPromesa.objects.get(token= token)
        form = RegistracionUsuarioForm(initial={"last_name": up.last_name,"first_name":up.first_name, "username":up.username,"email":up.email})
        contexto = {'form': form,}
    else:
        if request.method=='POST':
            form = RegistracionUsuarioForm(request.POST)
            print ("paso por el submit")
            if form.is_valid():
                form.save()
                us = form.cleaned_data["username"]
                up = UsuarioPromesa.objects.get(username=us)
                up.delete()
                messages.success(request, 'El usuario fue creado correctamente.')
                return redirect("/accounts/login/", )
            else:
                contexto = {'form': form,}

    return render(request, "registration/activacionUsuario.html", contexto)
