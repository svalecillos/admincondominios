# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroPago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('referencia', models.CharField(max_length=10, unique=True)),
                ('fecha', models.DateTimeField(default='2016-01-22 18:20:29-04:30')),
                ('comentario', models.CharField(max_length=140)),
            ],
            options={
                'verbose_name': 'Registro de pago',
                'verbose_name_plural': 'Registro de pagos',
            },
        ),
        migrations.CreateModel(
            name='TipoDePago',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('tipoDePago', models.CharField(max_length=100, verbose_name='Tipo de pagos', unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de pago',
                'verbose_name_plural': 'Tipo de pagos',
            },
        ),
    ]
