# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from models import Proveedores

# Metodo para insertar Proveedores
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
    return render(request, 'consultarProveedores.html', {'registros':registroProveedores})
