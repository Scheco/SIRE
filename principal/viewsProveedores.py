# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from models import Proveedores


def insertar(request):
    if 'id' in request.POST and 'nombre' in request.POST and 'apellidoP' in request.POST and 'nombreM' in request.POST and 'edad' in request.POST and 'telefono' in request.POST and 'Domicilio' in request.POST:
            idProveedores = request.POST['id']
            nombre = request.POST['nombre']
            apellidoP = request.POST['apellidoP']
            apellidoM = request.POST['apellidoM']
            edad = request.POST['edad']
            telefono = request.POST['telefono']
            domicilio = request.POST['domicilio']
            p = Proveedores(idProveedores = idProveedores, nombre = nombre, apellidoP = apellidoP, apellidoM = apellidoM, edad = edad, telefono = telefono, domicilio = domicilio)
            p.save()
            return render(request, 'insertarProveedores.html', {'msg': 'Se registraron correctamente todos los datos del proveedor', 'p':p})
    else:
        return render(request, 'insertarProveedores.html')
