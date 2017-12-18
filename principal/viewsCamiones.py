# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Camiones
from models import Trabajadores

# Metodo para registrar camion
def insertarCamion(request):
    if 'idTrabajador' in request.POST and 'modelo' in request.POST and 'marca' in request.POST and 'anio' in request.POST:
            c = Camiones(idTrabajador_id = request.POST['idTrabajador'], modelo = request.POST['modelo'], marca = request.POST['marca'], anio = request.POST['anio'])
            c.save()
            return render(request, 'insertarCamiones.html', {'msg': 'Se registraron correctamente todos los datos del camion', 'c':c})
    else:
        trabajadores = Trabajadores.objects.all()
        return render(request, 'insertarCamiones.html', {'trabajadores':trabajadores})

# Metodo para consultar todos los datos de los camiones ya registrados
def consultarCamion(request):
    camiones = Camiones.objects.all()
    return render(request, 'consultarCamiones.html', {'registroCamiones':camiones})



# Metodo para mostrar todos los datos de los camiones para modificar
def modificarCamion(request):
    camion = Camiones.objects.get(idCamion=request.POST['idCamion'])
    return render (request, 'modificarCamiones.html', {'reg':camion})

# Metodo para guardar uno o mas cambios en la vista de modificarCamiones.html
def guardarCamion(request):
    c = Camiones(idCamion = request.POST['idCamion'], idTrabajador = request.POST['idTrabajador'], modelo = request.POST['modelo'], marca = request.POST['marca'], anio = request.POST['anio'])
    c.save()
    registroCamiones = camiones.objects.all()
    return render(request, 'consultarCamiones.html', {'msg': 'Se ha actualizado el registro correctamente','registroCamiones':registroCamiones})

# Metodo para eliminar camion
def eliminarCamion(request):
    c = Camiones(idCamion = request.POST['idCamion'])
    c.delete()
    registroCamiones = Camiones.objects.all()
    return render(request, 'consultarCamiones.html', {'msg': 'Se ha eliminado el registro correctamente', 'registroCamiones':registroCamiones})

# Metodo para confirmar eliminacion del camion con el id
def feliminarCamion(request):
    idCamion = request.GET['idCamion']
    return render(request, 'eliminarCamiones.html', {'idCamion':idCamion})
