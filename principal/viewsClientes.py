# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Clientes
from models import Materiales


def insertarClientes(request):
    if 'idCliente' in request.POST and 'idMaterial' in request.POST and 'nombre' in request.POST and 'apellidoP' in request.POST and 'apellidoM' in request.POST and 'domicilio' in request.POST and 'telefono' in request.POST:
            idClientes = request.POST['idCliente']
            idMaterial = request.POST['idMaterial']
            nombre = request.POST['nombre']
            apellidoP = request.POST['apellidoP']
            apellidoM = request.POST['apellidoM']
            domicilio = request.POST['domicilio']
            telefono = request.POST['telefono']
            Cl = Clientes(idCliente=idClientes,idMaterial_id=idMaterial,nombre=nombre,apellidoP=apellidoP,apellidoM=apellidoM,domicilio=domicilio,telefono=telefono)
            Cl= save()
            return render(request,'menu.html')
    else:
        return render(request,'insertarClientes.html')
