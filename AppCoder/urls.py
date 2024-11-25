from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio/', views.inicio, name ="inicio"),
    path('Vendedores/', views.Vendedores, name="Vendedores"),
    path('Clientes/', views.Clientes, name="Clientes"),
    path('Productos/', views.productos, name="Productos"),
    path('Entregados/', views.Entregados, name="Entregados"),
    path('vendedor_form/', views.vendedor_form, name="vendedor_form"),
    path('Vendedor_form2/', views.Vendedor_form2, name="Vendedor_form2"),
    path('Cliente_form3/', views.Cliente_form3, name="Cliente_form3"),
    path('Productos_form4/', views.Productos_form4, name="Productos_form4"),
    path('Entregado_form5/', views.Entregado_form5, name="Entregado_form5"),
    path('busqueda_Vendedor/', views.busquedaVendedor, name="busqueda_Vendedor"),
    path('buscar/', views.buscar),
]