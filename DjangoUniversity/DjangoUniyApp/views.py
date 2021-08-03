from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse, request

def index(request):
    context= {'clase': 'Aprendiendo Django','curso':'ADSI'}
    return render(request,'listado_estudiante.html', context)

def estudiante(request,pk):
    return HttpResponse("El estudiante es: ",pk)

def ejemplo_view(request):
    return render(request, 'ejemplo.html', locals())
# Create your views here.
