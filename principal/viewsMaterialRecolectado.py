# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import MaterialRecolectado
from models import Materiales
from models import Camiones
from models import Negocios

# Metodo para registrar MaterialRecolectado
def insertarMaterialRecolectado(request):
    if 'idMaterial' in request.POST and 'idCamion' in request.POST and 'idNegocio' in request.POST and 'peso' in request.POST and 'fecha' in request.POST:
            M = MaterialRecolectado(idMaterial_id = request.POST['idMaterial'], idCamion_id = request.POST['idCamion'], idNegocio_id = request.POST['idNegocio'], peso = request.POST['peso'], fecha = request.POST['fecha'])
            M.save()
            return render(request, 'insertarMaterialRecolectado.html', {'msg': 'Se registraron correctamente todos los datos'})
    else:
        material = Materiales.objects.all()
        camiones = Camiones.objects.all()
        negocios = Negocios.objects.all()
        return render(request, 'insertarMaterialRecolectado.html', {'material':material,'camiones':camiones,'negocios':negocios})

# Metodo para consultar todos los datos de los MaterialRecolectado ya registrados
def consultarMaterialRecolectado(request):
    materialRecolectado = MaterialRecolectado.objects.all()
    return render(request, 'consultarMaterialRecolectado.html', {'materialRecolectado':materialRecolectado})

# Metodo para mostrar todos los datos de materialRecolectado para modificar
def modificarMaterialRecolectado(request):
    materialRecolectado = MaterialRecolectado.objects.get(idMaterialRecolectado=request.POST['idMaterialRecolectado'])
    material = Materiales.objects.all()
    camiones = Camiones.objects.all()
    negocios = Negocios.objects.all()
    return render(request, 'insertarMaterialRecolectado.html', {'materialRecolectado':materialRecolectado,'material':material,'camiones':camiones,'negocios':negocios})

# Metodo para guardar uno o mas cambios en la vista de modificarMaterialRecolectado.html
def guardarMaterialRecolectado(request):
    M = MaterialRecolectado(idMaterial_id = request.POST['idMaterial'], idCamion_id = request.POST['idCamion'], idNegocio_id = request.POST['idNegocio'], peso = request.POST['peso'], fecha = request.POST['fecha'])
    M.save()
    materialRecolectado = MaterialRecolectado.objects.all()
    return render(request, 'consultarMaterialRecolectado.html', {'msg': 'Se ha actualizado el registro correctamente','materialRecolectado':materialRecolectado})

# Metodo para eliminar materialRecolectado
def eliminarMaterialRecolectado(request):
    M = MaterialRecolectado(idMaterialRecolectado_id = request.POST['idMaterialRecolectado'])
    M.delete()
    materialRecolectado = MaterialRecolectado.objects.all()
    return render(request, 'consultarMaterialRecolectado.html', {'msg': 'Se ha eliminado el registro correctamente', 'materialRecolectado':materialRecolectado})

# Metodo para confirmar eliminacion del camion con el id
def feliminarMaterialRecolectado(request):
    idMaterialRecolectado = request.GET['idMaterialRecolectado']
    return render(request, 'eliminarMaterialRecolectado.html', {'idMaterialRecolectado':idMaterialRecolectado})
