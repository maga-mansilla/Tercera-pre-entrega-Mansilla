from django.db import models

# Create your models here.

class Libro(models.Model):
    Autor = models.CharField(max_length=40)
    Categoria = models.CharField(max_length=40)
    cantidad_paginas = models.IntegerField()

class Bibliotecaria(models.Model):
    nombre = models.CharField(max_length=40)
    
class Lector(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_de_retiro = models.DateField()
    fecha_de_entrega = models.DateField()

class Entregado(models.Model):
    Entregado = models.BooleanField()

