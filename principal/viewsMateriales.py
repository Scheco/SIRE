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
