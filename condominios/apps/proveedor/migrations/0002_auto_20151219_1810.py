# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20151219_1548'),
        ('proveedor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='servicios_especiales',
            field=models.ManyToManyField(to='servicio.ServicioEspecial'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='servicios_mensuales',
            field=models.ManyToManyField(to='servicio.ServicioMensual'),
        ),
    ]
