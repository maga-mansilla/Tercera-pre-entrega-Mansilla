from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Vendedor,Cliente,Productos,Entregado
from AppCoder.forms import Vendedor_formulario2, Cliente_formulario3,Productos_formulario4,Entregado_formulario5

# Create your views here.
def inicio(req):
    return render(req,"appcoder/padre.html")
def Vendedores(req):
    return render(req,"appcoder/Vendedores.html")
def productos(req):
    return render(req,"appcoder/productos.html")
def Clientes(req):
    return render(req,"appcoder/Clientes.html")
def Entregados(req):
    return render(req,"appcoder/Entregados.html")

#FORMULARIO HTML

def vendedor_form(req):
    if req.method == 'POST':
      
            vendedor = Vendedor(Nombre=req.POST['Nombre'],Turno=req.POST['Turno'],Monto_caja=req.POST['Monto_caja'])
 
            vendedor.save()
 
            return render(req, "AppCoder/Datoingresado.html")
 
    return render(req,"AppCoder/vendedorformulario.html")

#FORMULARIOS POR DJANGO

def Vendedor_form2(request):
    if request.method == "POST":  
        miFormulario = Vendedor_formulario2(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            vendedor = Vendedor(Nombre=informacion["Nombre"], Turno=informacion["Turno"], Monto_caja=informacion["Monto_caja"])  # Creamos un objeto Curso
            vendedor.save()  
            return render(request, "AppCoder/Datoingresado.html")  
    else:
        miFormulario = Vendedor_formulario2()  

    return render(request, "AppCoder/Vendedor_formulario2.html", {"miFormulario": miFormulario})

def Cliente_form3(request):
    if request.method == "POST":  
        miFormulario = Cliente_formulario3(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            cliente = Cliente(nombre=informacion["nombre"], email=informacion["email"], fecha_de_pedido=informacion["fecha_de_pedido"])  
            cliente.save()  
            return render(request, "AppCoder/Datoingresado.html")  
    else:
        miFormulario = Cliente_formulario3()  

    return render(request, "AppCoder/Cliente_formulario3.html", {"miFormulario": miFormulario})

def Productos_form4(request):
    if request.method == "POST":  
        miFormulario = Productos_formulario4(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            producto = Productos(nombre=informacion["nombre"], precio=informacion["precio"])  
            producto.save()  
            return render(request, "AppCoder/Datoingresado")  
    else:
        miFormulario = Productos_formulario4()  

    return render(request, "AppCoder/Productos_formulario4.html", {"miFormulario": miFormulario})


def Entregado_form5(request):
    if request.method == "POST":  
        miFormulario = Entregado_formulario5(request.POST) 
        print(miFormulario)

        if miFormulario.is_valid():  
            informacion = miFormulario.cleaned_data  
            entregado = Entregado(entregado=informacion["entregado"])  
            entregado.save()  
            return render(request, "AppCoder/Datoingresado.html")  
    else:
        miFormulario = Entregado_formulario5()  

    return render(request, "AppCoder/Entregado_formulario5.html", {"miFormulario": miFormulario})

#BUSQUEDA EN BASE DE DATOS


def busquedaVendedor(request):
     return render(request, "AppCoder/busquedaVendedor.html")

def buscar(request):

    if request.GET["Nombre"]:

        
        Nombre = request.GET['Nombre']

        Vendedores = Vendedor.objects.filter(Nombre__icontains=Nombre)

        return render(request, "AppCoder/resultadosbusqueda.html", {"Vendedores": Vendedores, "Nombre": Nombre})

    else:

        respuesta = "No enviaste datos"

    return HttpResponse(respuesta)

