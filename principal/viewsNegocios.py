# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Proveedores
from models import Negocios

def insertarNegocios(request):
    if  "idProveedor" in request.POST and "nombreNegocio" in request.POST and "domicilio" in request.POST and "tel" in request.POST:
            idProveedor= request.POST['idProveedor']
            nombreNegocio= request.POST['nombreNegocio']
            domicilio= request.POST['domicilio']
            tel=request.POST['tel']
            Ne=Negocios(nombre=nombreNegocio,domicilio=domicilio,telefono=tel,idProveedores_id=idProveedor)
            Ne.save()
            # negocios=Negocios.objects.get['idNegocio']
            # return render(request,'insertarNegocios.html',{'msg': 'Se registro correctamente un nuevo negocio '+' Nombre '+Ne.nombre+"id"+negocios , 'Ne':Ne})
            return render(request,'insertarNegocios.html',{'msg': 'Se registro correctamente un nuevo negocio '+' Nombre '+Ne.nombre , 'Ne':Ne})
    else:
        return render(request,'insertarNegocios.html')

def consultarNegocios(request):
    negocios=Negocios.objects.all()
    proveedores=Proveedores.objects.all()
    return render(request,'consultarNegocios.html',{'registroNegocios':negocios,'registroProveedores':proveedores})

def modificarNegocios(request):
    registro=Negocios.objects.get(idNegocio=request.POST['idNegocio'])
    return render(request,'modificarNegocios.html',{'regNe':registro})

def guardarNegocios(request):
    Ne=Negocios(idNegocio = request.POST['idNegocio'])
    Ne.idProveedores_id = request.POST['idProveedor']
    Ne.nombre = request.POST['nombre']
    Ne.domicilio = request.POST['domicilio']
    Ne.telefono = request.POST['telefono']
    Ne.save()
    negocios=Negocios.objects.all()
    proveedores=Proveedores.objects.all()
    return render(request,'consultarNegocios.html',{'msg': 'Se ha actualizo el registro correctamente el ID: '+Ne.idNegocio +' Nombre '+Ne.nombre,'registroNegocios':negocios,'registroProveedores':proveedores})


def eliminarNeg(request):
    idNegocio=request.GET['idNegocio']
    return render(request,'eliminarNegocios.html',{'idNegocio':idNegocio})

def eliminarNegocios(request):
    Ne= Negocios(idNegocio = request.POST['idNegocio'])
    Ne.delete()
    negocios= Negocios.objects.all()
    proveedores=Proveedores.objects.all()
    return render(request,'consultarNegocios.html',{'msg': 'Se ha eliminado el negocio correctamente','registroNegocios':negocios,'registroProveedores':proveedores})
