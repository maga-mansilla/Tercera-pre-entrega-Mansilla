from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(req):
    return render(req,"appcoder/padre.html")
def Vendedor(req):
    return render(req,"appcoder/Vendedor.html")
def Productos(req):
    return render(req,"appcoder/Productos.html")
def Cliente(req):
    return render(req,"appcoder/Cliente.html")
def Entregado(req):
    return render(req,"appcoder/Entregado.html")