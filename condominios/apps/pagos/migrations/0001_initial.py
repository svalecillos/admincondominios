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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.DecimalField(max_digits=10, decimal_places=2)),
                ('referencia', models.CharField(unique=True, max_length=10)),
                ('fecha', models.DateTimeField()),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoDePago', models.CharField(unique=True, max_length=100, verbose_name=b'Tipo de pagos')),
            ],
            options={
                'verbose_name': 'Tipo de pago',
                'verbose_name_plural': 'Tipo de pagos',
            },
        ),
    ]
