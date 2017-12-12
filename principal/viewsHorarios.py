from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from models import Horarios

def insertarHorario(request):
    return render(request,"insertarHorario.html")
