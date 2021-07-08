from django.urls import path
from .views import crearClientes, index, galeria, clientes, form_mod_cliente, form_del_cliente

urlpatterns = [
    path('', index, name="index"),
    path('galeria', galeria, name="galeria"),
    path('clientes', clientes, name="clientes"),
    path('crearClientes', crearClientes, name="crearClientes"),
    path('form_mod_cliente/<id>', form_mod_cliente, name="form_mod_cliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente")

]