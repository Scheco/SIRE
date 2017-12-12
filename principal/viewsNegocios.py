# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


from models import Proveedores
from models import Negocios

def insertarNegocio(request):
    if "idNegocio" in request.POST and "idProveedor" in request.POST and "nombreNegocio" in request.POST and "domicilio" in request.POST and "tel" in request.POST:
            idNegocio = request.POST['idNegocio']
            idProveedor= request.POST['idProveedor']
            nombreNegocio= request.POST['nombreNegocio']
            domicilio= request.POST['domicilio']
            tel=request.POST['tel']
            Ne=Negocios(idNegocio=idNegocio,nombre=nombreNegocio,domicilio=domicilio,telefono=tel,idProveedores_id=idProveedor)
            Ne.save()
            return render(request,'insertarNegocio.html')
    else:
        return render(request,'insertarNegocio.html')
