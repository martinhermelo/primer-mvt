from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render



def welcome(request):
    return HttpResponse("Bienvenido a esta Pagina. Espero que te entretengas navengando aqui. Un paso mas para saber programar")

def hora(request):
    hora= datetime.today().time()
    return HttpResponse(f"Son las {hora}hs")

def tipeo(request):
    return render(request, "tipeo.html", context={})

def segundo_intento(request):
    context={
        "name" : "Martin",
        "last_name" : "Hermelo",
    }
    return render(request, "segundo_tipeo.html", context=context)