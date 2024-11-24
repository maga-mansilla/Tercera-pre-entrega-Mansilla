from django.contrib import admin
from AppCoder.models import Vendedor, Cliente, Entregado, Productos

# Register your models here.
admin.site.register(Vendedor)
admin.site.register(Cliente)
admin.site.register(Productos)
admin.site.register(Entregado)

