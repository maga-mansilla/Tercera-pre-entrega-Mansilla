from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Vendedor
#from AppCoder.forms import Vendedor_formulario2

# Create your views here.
def inicio(req):
    return render(req,"appcoder/padre.html")
def Vendedores(req):
    return render(req,"appcoder/Vendedores.html")
def Productos(req):
    return render(req,"appcoder/Productos.html")
def Clientes(req):
    return render(req,"appcoder/Clientes.html")
def Entregados(req):
    return render(req,"appcoder/Entregados.html")

def vendedor_form(req):
    if req.method == 'post':
      
            vendedor = Vendedor(Nombre=req.POST['Nombre'],Turno=req.POST['Turno'],Monto_caja=req.POST['Monto_caja'])
 
            vendedor.save()
 
            return render(req, "AppCoder/index.html")
 
    return render(req,"AppCoder/vendedorformulario.html")

#def Vendedor_formulario2(request):

    #if request.method == "POST":  # Si el formulario fue enviado
        #miFormulario = Vendedor_formulario2(request.POST)  # Creamos un objeto formulario con los datos enviados
        #print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        #if miFormulario.is_valid():  # Verificamos si los datos son válidos
            #informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            #vendedor = Vendedor(nombre=informacion["Nombre"], turno=informacion["Turno"], monto_caja=informacion["Monto_caja"])  # Creamos un objeto Curso
            #vendedor.save()  # Guardamos el curso en la base de datos
            #return render(request, "AppCoder/index.html")  # Redirigimos a la página de inicio
    #else:
        #miFormulario = Vendedor_formulario2()  # Creamos un formulario vacío para mostrarlo inicialmente

    #return render(request, "AppCoder/Vendedor_formulario2.html", {"miFormulario": miFormulario})

