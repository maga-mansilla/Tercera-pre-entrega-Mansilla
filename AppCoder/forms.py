from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}