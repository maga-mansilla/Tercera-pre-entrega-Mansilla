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
    path('leerClientes/', views.leerClientes, name="leerClientes"),
    path('EliminarCliente/<cliente_nombre>/', views.EliminarCliente, name="EliminarCliente"),
    path('EditarCliente/<cliente_nombre>/', views.EditarCliente, name="EditarCliente"),
    path('lista/', views.VendedorListView.as_view(), name='List'),
    path('detalle/<int:pk>/', views.VendedorDetalle.as_view(), name='Detail'),
    path('nuevo/', views.VendedorCreateView.as_view(), name='New'),
    path('editar/<int:pk>/', views.VendedorUpdateView.as_view(), name='Edit'),
    path('eliminar/<int:pk>/', views.VendedorDeleteView.as_view(), name='Delete'),
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name='register'),
]