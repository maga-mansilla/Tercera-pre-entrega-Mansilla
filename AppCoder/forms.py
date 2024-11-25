from django import forms

class Vendedor_formulario2(forms.Form):
    nombre = forms.CharField(max_length=20)
    turno = forms.CharField()


    