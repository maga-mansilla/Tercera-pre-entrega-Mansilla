from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio/', views.inicio, name ="inicio"),
    path('Vendedor/', views.Vendedor, name="Vendedor"),
    path('Cliente/', views.Cliente, name="Cliente"),
    path('Producto/', views.Productos, name="Productos"),
    path('Entregados/', views.Entregado, name="Entregado"),

    
]