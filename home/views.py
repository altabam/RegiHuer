from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth.models import User
import hashlib, datetime, random, os
from .models import UsuarioPromesa
from .forms import RegistracionUsuarioForm, UsuarioPromesaForm
# Create your views here.
def index(request):
    return render(request, "index.html")

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
    upun = User.objects.filter(username=form.cleaned_data['username'])
    upem = User.objects.filter(email = form.cleaned_data['email'])
    bandera = True
    print("no se si paso por aca")
    if(upun):
        messages.error(request, 'El nombre de usuario se encuentra registrado')
        bandera = False
    if(upem):
        messages.error(request, 'El email de usuario se encuentra registrado')
        bandera = False
    
    if(bandera):
        form.save()
        up = UsuarioPromesa.objects.get(username = un)
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
