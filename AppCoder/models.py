from django.db import models

# Create your models here.

class Vendedor(models.Model):
    Nombre = models.CharField(max_length=40)
    Turno = models.CharField(max_length=40)
    Monto_caja = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.Nombre} - Turno: {self.Turno} - Monto_caja: {self.Monto_caja}"

class Productos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.FloatField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Precio: {self.precio} "


class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_de_pedido= models.DateField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Email: {self.email} - Fecha_de_pedido: {self.fecha_de_pedido}"

class Entregado(models.Model):
    entregado = models.BooleanField()

