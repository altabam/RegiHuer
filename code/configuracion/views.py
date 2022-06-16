from urllib import response, request
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola Mundo, Bienvenidos a la app Registro de Huertas ")

def consultaPersona(request, persona_id):
    return HttpResponse("Estas mirando la persona: %s." % persona_id )