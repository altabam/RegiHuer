from django.shortcuts import render
from urllib import response, request
# Create your views here.

# Create your views here.
def login(request):
    contexto = {
        "ocultarLogin":"true"

    }
    print("login", contexto)
    return render(request, "login.html",contexto)
