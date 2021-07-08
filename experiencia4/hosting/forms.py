from django import forms
from django.forms import ModelForm, widgets
from .models import Cliente, Categoria

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['numeroId','nombreCompleto', 'telefono', 'direccion', 'email', 'pais', 'contrasena', 'moneda']

        labels={
            'numeroId': 'ID',
            'nombreCompleto': 'Nombre completo', 
            'telefono': 'Teléfono', 
            'direccion': 'Dirección',
            'email': 'Email',
            'pais': 'País',
            'contrasena': 'Contraseña',
            'moneda': 'Moneda',
        }

        widgets={
            'numeroId': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su número de identificación ', 
                    'id': 'numeroId'
                }
            ),
            'nombreCompleto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su nombre completo', 
                    'id': 'nombreCompleto'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su teléfono', 
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su dirección', 
                    'id': 'direccion'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su Email', 
                    'id': 'email'
                }
            ),
            'pais': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su país', 
                    'id': 'pais'
                }
            ),
            'contrasena': forms.PasswordInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese su contraseña', 
                    'id': 'contrasena'
                }
            ),
            'moneda': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pesos o Dólares', 
                    'id': 'moneda'
                }
            )
        }