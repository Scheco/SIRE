# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from models import Proveedores
from models import Negocios
from models import Horarios
from models import Trabajadores
from models import Camiones
from models import Materiales
from models import MaterialRecolectado
from models import Clientes
from models import Ventas


def menu(request):
    return render(request,'menu.html')
