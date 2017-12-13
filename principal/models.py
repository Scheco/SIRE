# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Proveedores(models.Model):
    idProveedores = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=10)
    domicilio = models.CharField(max_length=50)

class Negocios(models.Model):
    idNegocio = models.AutoField(primary_key=True)
    idProveedores = models.ForeignKey(Proveedores)
    nombre = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)

class Horarios(models.Model):
    idHorario = models.IntegerField(primary_key=True)
    idNegocio = models.ForeignKey(Negocios)
    lunes = models.BooleanField(default=True)
    horaLunes = models.TimeField(null=False)
    martes = models.BooleanField(default=False)
    horaMartes = models.TimeField(null=False)
    miercoles = models.BooleanField(default=False)
    horaMiercoles = models.TimeField(null=False)
    jueves = models.BooleanField(default=False)
    horaJueves = models.TimeField(null=False)
    viernes = models.BooleanField(default=False)
    horaViernes = models.TimeField(null=False)
    sabado = models.BooleanField(default=False)
    horaSabado = models.TimeField(null=False)

class Trabajadores(models.Model):
    idTrabajador = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)
    edad = models.CharField(max_length=2)
    telefono = models.CharField(max_length=10)
    licencia = models.CharField(null=True, max_length=100)

class Camiones(models.Model):
    idCamion = models.IntegerField(primary_key=True)
    idTrabajador = models.ForeignKey(Trabajadores)
    modelo = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    anio = models.CharField(max_length=4)

class Materiales(models.Model):
    idMaterial = models.IntegerField(primary_key=True)
    tipo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

class MaterialRecolectado(models.Model):
    idMaterialRecolectado = models.IntegerField(primary_key=True)
    idMaterial = models.ForeignKey(Materiales)
    idCamion = models.ForeignKey(Camiones)
    idNegocio = models.ForeignKey(Negocios)
    peso = models.FloatField(max_length=7)
    fecha = models.DateField()

class Clientes(models.Model):
    idCliente = models.IntegerField(primary_key=True)
    idMaterial = models.ForeignKey(Materiales)
    nombre = models.CharField(max_length=30)
    apellidoP = models.CharField(max_length=30)
    apellidoM = models.CharField(max_length=30)
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

class Ventas(models.Model):
    idVenta = models.IntegerField(primary_key=True)
    idCliente = models.ForeignKey(Clientes)
    idMaterialRecolectado = models.ForeignKey(MaterialRecolectado)
    precio = models.FloatField(max_length=10)
    fecha = models.DateField()
