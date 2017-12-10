# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idProveedores = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.IntegerField()
    domicilio = models.CharField(max_length=50)

class Negocios(models.Model):
    idNegocio = models.IntegerField(primary_key=True)
    idProveedores = models.ForeignKey(Proveedores)
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.IntegerField()
