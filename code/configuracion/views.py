from urllib import response, request
from django.shortcuts import render
from django.template import loader
from .models import Hortelano
# Create your views here.
from django.http import HttpResponse


def index(request):
    listaHortelanos = Hortelano.objects.all()
    template = loader.get_template('index.html')
    context = {
        'listaHortelanos': listaHortelanos,
    }
    return HttpResponse(template.render(context, request))
    
    
def consultaPersona(request, persona_id):
    return HttpResponse("Estas mirando la persona: %s." % persona_id )