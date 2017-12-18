# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import MaterialRecolectado

def insertarMaterialesRecolectados(request):
    if "idMaterialRecolectado" in request.POST and  "peso" in request.POST and "fecha" in request.POST and "idCamion" in request.POST and "idMaterial" in request.POST and "idNegocio" in request.POST:
            idMaterialRecolectado = request.POST['idMaterialRecolectado']
            peso = request.POST['peso']
            fecha = request.POST['fecha']
            idCamion = request.POST['idCamion']
            idMaterial = request.POST['idMaterial']
            idNegocio = request.POST['idNegocio']
            MR = MaterialRecolectado(idMaterialRecolectado=idMaterialRecolectado,peso=peso,fecha=fecha,idCamion_id=idCamion,idMaterial_id=idMaterial,idNegocio_id=idNegocio)
            MR.save()
            return render(request,'insertarMaterialRecolectado.html')
    else:
        return render(request,'insertarMaterialRecolectado.html')
