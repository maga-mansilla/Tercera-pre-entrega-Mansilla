from django.db import models

# Create your models here.

class Vendedor(models.Model):
    Nombre = models.CharField(max_length=40)
    Turno = models.CharField(max_length=40)
    Monto_caja = models.IntegerField()

class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    fecha_entrega = models.DateField
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_de_pedido= models.DateField()

class Entregado(models.Model):
    Entregado = models.BooleanField()

