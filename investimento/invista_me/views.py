from django.shortcuts import render
from django.shortcuts import HttpResponse

def pagina_inicial(request):
    return HttpResponse("investimento!")
# Create your views here.
def contato(request):
    return HttpResponse("Contato")