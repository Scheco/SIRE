# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Trabajadores


def insertarTrabajador(request):
    if  'Nombre' in request.POST and 'Apellido_p' in request.POST and 'Apellido_m' in request.POST and 'Tipo' in request.POST and 'Edad' in request.POST and 'Telefono' in request.POST and 'Licencia' in request.POST:
        nombre = request.POST['Nombre']
        apellidoP = request.POST['Apellido_p']
        apellidoM = request.POST['Apellido_m']
        tipo = request.POST['Tipo']
        edad = request.POST['Edad']
        telefono = request.POST['Telefono']
        licencia = request.POST['Licencia']
        p=Trabajadores(nombre=nombre,apellidoP=apellidoP,apellidoM=apellidoM,tipo=tipo,edad=edad,telefono=telefono,licencia=licencia)
        p.save()
        return render(request,'insertarTrabajadores.html')
    else:
        return render(request,'insertarTrabajadores.html')


def trabajadores(request):
    return render(request,'insertarTrabajadores.html')

def consultarTrabajadores(request):
    consulta=Trabajadores.objects.all()
    return render(request, 'consultaTrabajadores.html',{'Trabajadores':consulta})

def modificarTrabajadores(request):
        registro = Trabajadores.objects.get(idTrabajador=request.POST['idTrabajador'])
        return render (request, 'modificarTrabajador.html', {'reg':registro})

def feliminarTrabajador(request):
            idTrabajador = request.GET['idTrabajador']
            return render(request, 'eliminarTrabajadores.html', {'idTrabajador':idTrabajador})
