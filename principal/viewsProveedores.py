# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from models import Proveedores

def insertarProveedores(request):
    if  'nombreProveedor' in request.POST and 'apellidoP' in request.POST and 'apellidoM' in request.POST and 'edad' in request.POST and 'telefono' in request.POST and 'domicilio' in request.POST:
            nombreProveedor = request.POST['nombreProveedor']
            apellidoP = request.POST['apellidoP']
            apellidoM = request.POST['apellidoM']
            edad = request.POST['edad']
            telefono = request.POST['telefono']
            domicilio = request.POST['domicilio']
            p = Proveedores(nombre = nombreProveedor, apellidoP = apellidoP, apellidoM = apellidoM, edad = edad, telefono = telefono, domicilio = domicilio)
            p.save()
            return render(request, 'insertarProveedores.html', {'msg': 'Se registraron correctamente todos los datos del proveedor', 'p':p})
    else:
        return render(request, 'insertarProveedores.html')


def consultarProveedores(request):
    registroProveedores = Proveedores.objects.all()
    return render(request, 'consultarProveedores.html', {'registroProveedores':registroProveedores})


def modificarProveedores(request):
    registro = Proveedores.objects.get(idProveedores=request.POST['idProveedores'])
    return render (request, 'modificarProveedores.html', {'reg':registro})


def guardarProveedores(request):
    p = Proveedores(idProveedores = request.POST['idProveedores'])
    p.nombre = request.POST['nombreProveedor']
    p.apellidoP = request.POST['apellidoP']
    p.apellidoM = request.POST['apellidoM']
    p.edad = request.POST['edad']
    p.telefono = request.POST['telefono']
    p.domicilio = request.POST['domicilio']
    p.save()
    registroProveedores = Proveedores.objects.all()
    return render(request, 'consultarProveedores.html', {'msg': 'Se ha actualizado el registro correctamente','registroProveedores':registroProveedores})


def feliminarProveedor(request):
    idProveedores = request.GET['idProveedores']
    return render(request, 'eliminarProveedores.html', {'idProveedores':idProveedores})


def eliminarProveedor(request):
    p = Proveedores(idProveedores = request.POST['idProveedores'])
    p.delete()
    registroProveedores = Proveedores.objects.all()
    return render(request, 'consultarProveedores.html', {'msg': 'Se ha eliminado el registro correctamente', 'registroProveedores':registroProveedores})
