from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import Vendedor,Cliente,Productos,Entregado
from AppCoder.forms import Vendedor_formulario2, Cliente_formulario3,Productos_formulario4,Entregado_formulario5
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Formularios de autenticación de usuarios
from django.contrib.auth import login, logout, authenticate  # Funciones para gestionar inicios de sesión y autenticación
from .forms import UserRegisterForm


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

def leerClientes(request):

    clientes= Cliente.objects.all()
    contexto= {"clientes":clientes}
    return render(request, "AppCoder/leerClientes.html", contexto)

def EliminarCliente(request,cliente_nombre):
    cliente= Cliente.objects.get(nombre=cliente_nombre)
    cliente.delete()
    Clientes = Cliente.objects.all()
    contexto = {"Clientes": Clientes}
    return render(request, "AppCoder/leerClientes.html", contexto)


def EditarCliente(request, cliente_nombre):

    try: 
        cliente = Cliente.objects.get(nombre=cliente_nombre)
    except Cliente.DoesNotExist:
        return render (request, 'error.html', {'mensaje':'cliente no encontrado'})

    if request.method == 'POST':

        miFormulario = Cliente_formulario3(request.POST)
        
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cliente.nombre = informacion['nombre']
            cliente.email = informacion['email']
            cliente.fecha_de_pedido = informacion ['fecha_de_pedido']

            cliente.save()
            return render(request, "AppCoder/index.html")
        
        else:
            return render (request,"AppCoder/EditarCliente.html", {"miFormulario": miFormulario, "cliente_nombre":cliente_nombre})
        
    else:
        miFormulario = Cliente_formulario3(initial={'nombre':cliente.nombre, 'email':cliente.email,'fecha_de_pedido':cliente.fecha_de_pedido})
        return render (request,"AppCoder/EditarCliente.html", {"miFormulario": miFormulario, "cliente_nombre":cliente_nombre})   
    
####### vistas basadas en clases###############

class VendedorListView(ListView):
    """
    Vista para mostrar una lista de todos los cursos.
    """
    model = Vendedor
    template_name = "AppCoder/vendedor_list.html"

class VendedorDetalle(DetailView):
    model = Vendedor
    template_name = "AppCoder/vendedor_detalle.html"

class VendedorCreateView(CreateView):
    model = Vendedor
    template_name = "AppCoder/vendedor_form.html"
    success_url =reverse_lazy("List")
    fields = ["Nombre", "Turno", "Monto_caja"]


class VendedorUpdateView(UpdateView):
    """
    vista para editar cursos a traves de un form.
    """
    model = Vendedor
    template_name = "AppCoder/vendedor_edit.html"
    success_url = reverse_lazy("List")
    fields = ["Nombre", "Turno", "Monto_caja"]

class VendedorDeleteView(DeleteView):
    """
    vista para eliminar cursos.
    """
    model = Vendedor
    success_url = reverse_lazy("List")
    template_name = "AppCoder/vendedor_confirm_delete.html"   


def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario y lo llena con los datos enviados
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            usuario = form.cleaned_data.get("username")  # Obtiene el nombre de usuario
            clave = form.cleaned_data.get("password")  # Obtiene la contraseña

            nombre_usuario = authenticate(username=usuario, password=clave)  # Intenta autenticar al usuario

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                return render(request, "AppCoder/padre.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  # Renderiza la plantilla con un mensaje de bienvenida
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                return render(request, "AppCoder/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            return render(request, "AppCoder/padre.html", {"mensaje":"Error, formulario inválido"})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "AppCoder/login.html", {"form":form})  # Renderiza el formulario de login

# Vista de registro
def register(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppCoder/index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()   

      return render(request,"AppCoder/registro.html" ,  {"form":form})



