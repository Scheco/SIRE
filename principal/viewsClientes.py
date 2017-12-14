# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Clientes
from models import Materiales


def insertarClientes(request):
    if "idCliente" in request.POST and "idMaterial" in request.POST and "nombre" in request.POST and "apellidoP" in request.POST and "apellidoM" in request.POST and "domicilio" in request.POST and "telefono" in request.POST:
            idCliente = request.POST['idCliente']
            idMaterial = request.POST['idMaterial']
            nombre = request.POST['nombre']
            apellidoP = request.POST['apellidoP']
            apellidoM = request.POST['apellidoM']
            domicilio = request.POST['domicilio']
            telefono = request.POST['telefono']
            Cl = Clientes(idCliente=idCliente,nombre=nombre,apellidoP=apellidoP,apellidoM=apellidoM,domicilio=domicilio,telefono=telefono,idMaterial_id=idMaterial)
            Cl.save()
            return render(request,'insertarClientes.html')
    else:
        return render(request,'insertarClientes.html')

def consultarClientes(request):
    registrosClientes = Clientes.objects.all()
    return render (request,'consultarClientes.html',{'registrosClientes':registrosClientes})

def modificarClientes(request):
    registroClientes = Clientes.objects.get(idCliente=request.POST['idCliente'])
    return render(request,'modificarClientes.html',{'reg':registroClientes})

def guardarCambiosClientes(request):
    Cl = Clientes(idCliente = request.POST['idCliente'])
    Cl.idMaterial=request.POST['idMaterial']
    Cl.nombre=request.POST['nombre']
    Cl.apellidoP=request.POST['apellidoP']
    Cl.apellidoM=request.POST['apellidoM']
    Cl.domicilio=request.POST['domicilio']
    Cl.telefono=request.POST['telefono']
    Cl.save()
    registrosClientes = Clientes.objects.all()
    return render (request, 'consultarClientes.html',{'msg':'Se ha actualizado el registro correctamente','registrosClientes':registrosClientes})
