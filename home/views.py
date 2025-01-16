from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.template.loader import render_to_string
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
            usuarioPromesa = generarUsuarioPromesa(form)
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
    url_app = "https://"+os.getenv("URL_APP")+ "/administracion/mailValidador?tk="+up.token
    print(url_app)
    print(up.fecha)
    un = up.username
    mensaje = render_to_string("registration/templateEmail.html",{'username':un, 'url_app':url_app})    # Enviar el correo
    print (mensaje)
    email = EmailMessage(
      subject='Bienvenido a nuestro sitio',
      body=mensaje,
      from_email='altabam@gmail.com',
      to=['altabam@yahoo.com.ar'],
    )
    
    email.content_subtype = 'html'  # Define el tipo como HTML
    email.send()
def generarUsuarioPromesa(form):
    form.save()
    un = form.cleaned_data['username']
    up = UsuarioPromesa.objects.get(username = un)
    alea = str(random.random())
    text = up.first_name + alea + up.username +str(up.fecha) + up.email + str(up.pk) + up.last_name 
    print(text)

    up.token = hashlib.sha256(text.encode()).hexdigest()
    up.aleatorio = alea
    print(up.token)
    print(up.aleatorio)
    up.save()
    #token = token_generator.make_token(form)
    
    return up  