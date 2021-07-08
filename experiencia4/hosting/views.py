from django.shortcuts import redirect, render
from .models import Categoria, Cliente
from .forms import ClienteForm

# Create your views here.
def index(request):
    return render (request, 'index.html')

def galeria(request):
    return render (request, 'galeria.html')

def clientes(request):
    
    clientes = Cliente.objects.all()
    return render(request, 'hosting/clientes.html', context={'datos': clientes})

def crearClientes(request):
    if request.method=='POST':
        cliente=ClienteForm(request.POST,request.FILES)
        if cliente.is_valid():
            cliente.save()
            return redirect('clientes')
    else:
        cliente=ClienteForm()
    return render(request, 'hosting/form_crearcliente.html', {'cliente': cliente})

def form_mod_cliente(request, id):
    cliente = Cliente.objects.get(numeroId=id)
    datos ={
        'form': ClienteForm(instance=cliente)
    }
    if request.method == 'POST': 
        formulario = ClienteForm(data=request.POST, instance = cliente,files=request.FILES)
        if formulario.is_valid: 
            formulario.save()
            datos['mensaje'] = "modificado correctamente"
            return redirect('clientes')
        datos['form'] = ClienteForm
    return render(request, 'hosting/form_mod_cliente.html', datos)

def form_del_cliente(request, id):
    cliente = Cliente.objects.get(numeroId=id)
    cliente.delete()
    return redirect(to="clientes")