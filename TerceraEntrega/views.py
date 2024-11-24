from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader

def saludo (request):
    return HttpResponse("<h1> ¡hola! </h1><p> soy maga.</p>")

def probandotemplate(request):

    Lista_de_notas = [10,1,5,6,8]
    nom = "juan"
    ap = "perez"
    diccionario_de_contexto = {"nombre": nom, "apellido": ap, "Notas": Lista_de_notas}

    plantilla = loader.get_template("template1.html")
    documento = plantilla.render(diccionario_de_contexto)
    #abrimos html

    #mi_html = open("./TerceraEntrega/plantillas/template1.html")

    #creamos el template haciendo uso de la clase template

    #plantilla = Template(mi_html.read())
    #cerramos el archivo, ya que lo tenemos cargado en la vble

    #mi_html.close()
    #creamos un contexto

    #mi_contexto = Context(diccionario_de_contexto)
    #terminamos de construir el context renderizandolo
    #documento = plantilla.render(mi_contexto)

    return HttpResponse(documento)
