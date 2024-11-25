from django import forms

class Vendedor_formulario2(forms.Form):
    Nombre = forms.CharField(max_length=20)
    Turno = forms.CharField(max_length=20)
    Monto_caja = forms.IntegerField()

class Cliente_formulario3(forms.Form):
    nombre = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=40)
    fecha_de_pedido = forms.DateField()

class Productos_formulario4(forms.Form):
    nombre = forms.CharField(max_length=40)
    precio = forms.FloatField()

class Entregado_formulario5(forms.Form):
     entregado = forms.BooleanField()



class Buscar(forms.Form):
    Nombre = forms.CharField(max_length=20)

    