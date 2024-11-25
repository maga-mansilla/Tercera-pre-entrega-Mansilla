from django.urls import path
from AppCoder import views


urlpatterns = [
    path('inicio/', views.inicio, name ="inicio"),
    path('Vendedores/', views.Vendedores, name="Vendedores"),
    path('Clientes/', views.Clientes, name="Clientes"),
    path('Productos/', views.Productos, name="Productos"),
    path('Entregados/', views.Entregados, name="Entregados"),
    path('vendedor_form/', views.vendedor_form, name="vendedor_form"),
    #path('Vendedor_formulario2/', views.Vendedor_formulario2, name="Vendedor_formulario2"),

    
]