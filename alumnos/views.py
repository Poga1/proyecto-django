from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request, 'alumnos/index.html', context)

def Carro(request):
    context={}
    return render(request, 'alumnos/Carro.html', context)

def contactanos(request):
    context={}
    return render(request, 'alumnos/contactanos.html', context)

def Login(request):
    context={}
    return render(request, 'alumnos/Login.html', context)

def Ropa(request):
    context={}
    return render(request, 'alumnos/Ropa.html', context)

def Registro(request):
    context={}
    return render(request, 'alumnos/Registro.html', context)