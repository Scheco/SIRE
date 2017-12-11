# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-11 01:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_materiales_materialrecolectado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellidoP', models.CharField(max_length=30)),
                ('apellidoM', models.CharField(max_length=30)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=10)),
                ('idMaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Materiales')),
            ],
        ),
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idVenta', models.IntegerField(primary_key=True, serialize=False)),
                ('precio', models.FloatField(max_length=10)),
                ('fecha', models.DateField()),
                ('idCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Clientes')),
                ('idMaterialRecolectado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.MaterialRecolectado')),
            ],
        ),
    ]
