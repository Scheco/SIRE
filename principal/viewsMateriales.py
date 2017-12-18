# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Materiales

def materiales(request):
    return render(request,'insertarMateriales.html')

def insertarMateriales(request):
    if 'tipoMaterial' in request.POST and 'descripcionMaterial' in request.POST:
            tipoMaterial = request.POST['tipoMaterial']
            descripcionMaterial = request.POST["descripcionMaterial"]
            m = Materiales(tipo=tipoMaterial, descripcion=descripcionMaterial)
            m.save()
            return render(request, 'insertarMateriales.html', {'msg': 'Se registro correctamente el material', 'm':m})
    else:
        return render(request, 'insertarMateriales.html')

def consultarMateriales(request):
    registros = Materiales.objects.all()
    return render (request,'consultarMateriales.html',{'registros':registros})

def modificarMateriales(request):
    m = Materiales(idMaterial=request.POST['id'])
    m.tipo = request.POST['tipo']
    m.descripcion = request.POST['descripcion']
    m.save()
    registros = Materiales.objects.all()
    return render(request,'consultarMateriales.html',{'msg':'Se han guardado los cambios correctamente','registros':registros})

def modificarM(request):
    registro = Materiales.objects.get(idMaterial=request.POST['id'])
    return render(request,'modificarMateriales.html',{'reg':registro})

def eliminarM(request):
    id = request.GET['id']
    return render(request,'eliminarMateriales.html',{'id':id})

def eliminarMateriales(request):
    m = Materiales(idMaterial=request.POST['id'])
    m.delete()
    registros = Materiales.objects.all()
    return render(request,'consultarMateriales.html',{'msg':'Se ha eliminado correctamente','registros':registros})
