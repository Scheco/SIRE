# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Materiales
from models import Clientes

def insertarClientes(request):
    if 'id' in request.POST and 'tipo' in request.POST and 'nombre' in request.POST and 'apellidoP' in request.POST and 'apellidoM' in request.POST and 'domicilio' in request.POST and 'telefono' in request.POST:
        idClientes = request.POST['id']
        tipoMaterial = request.POST['tipo']
        nombre = request.POST['nombre']
        apellidoPaterno = request.POST['apellidoP']
        apellidoMaterno = request.POST['apellidoM']
        domicilio = request.POST['domicilio']
        tel = request.POST['telefono']
        p = Clientes(idCliente=idClientes,idMaterial_id=tipoMaterial,nombre=nombre,apellidoP=apellidoPaterno,apellidoM=apellidoMaterno,domicilio=domicilio,telefono=tel)
        p = save()
        return render(request,'insertarClientes.html')
    else:
        return render(request,'insertarClientes.html')
