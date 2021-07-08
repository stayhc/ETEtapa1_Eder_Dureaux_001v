from django.db import models

# Create your models here.

class Categoria(models.Model):

    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre Categoría')

    def __str__(self):
        return self.nombreCategoria


class Cliente(models.Model):

    numeroId= models.CharField(max_length=9, primary_key=True, verbose_name='Numero de ID',null=True)
    nombreCompleto= models.CharField(max_length=20, verbose_name='Nombre del proveedor',null=True)
    telefono= models.CharField(max_length=20, verbose_name='Teléfono del proveedor',null=True)
    direccion= models.CharField(max_length=20, verbose_name='Dirección del proveedor',null=True)
    email = models.EmailField(verbose_name='Correo electrónico',null=True)
    pais = models.CharField(max_length=20, verbose_name='País del proveedor',null=True)
    contrasena = models.CharField(max_length=20, verbose_name='Contrasena',null=True,blank=True)
    moneda = models.CharField(max_length=20, verbose_name='Pesos o Dólares',null=True)

    def __str__(self):
        return self.numeroId