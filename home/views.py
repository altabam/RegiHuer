from django.shortcuts import render
from django.contrib import messages
from django.core.mail import EmailMessage

from .forms import RegistracionUsuarioForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def registrar(request):
    if request.method=='POST':
        form = RegistracionUsuarioForm(request.POST)
        print("no si es valido")
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            print("paso por form valido")
            enviarEmail(form)
            return render(request, "index.html")
    else:
        form = RegistracionUsuarioForm()
    contexto = {'form': form,}
    return render(request, "registration/registracion.html", contexto)

def enviarEmail(form):
    username = form.cleaned_data['username']
  
    # Renderizar la plantilla
    url_app = "https://"+ "/administracion/mailValidador"
    print(url_app)
    mensaje = '<h1>Hola {username} </h1> <p>Gracias por registrarte en nuestro sitio.</p> '
    # Enviar el correo
    email = EmailMessage(
      subject='Bienvenido a nuestro sitio',
      body=mensaje,
      from_email='altabam@gmail.com',
      to=['altabam@yahoo.com.ar'],
    )
    
    email.content_subtype = 'html'  # Define el tipo como HTML
    email.send()
  