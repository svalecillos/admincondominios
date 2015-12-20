# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0006_auto_20151219_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServicioEspecial',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('servicio_especial', models.CharField(max_length=50)),
                ('estatus', models.BooleanField()),
                ('condominio', models.ForeignKey(to='condominio.Condominio')),
            ],
            options={
                'verbose_name_plural': 'Servicios especiales',
            },
        ),
        migrations.CreateModel(
            name='ServicioMensual',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('servicio_especial', models.CharField(max_length=50)),
                ('estatus', models.BooleanField()),
                ('condominio', models.ForeignKey(to='condominio.Condominio')),
            ],
            options={
                'verbose_name_plural': 'Servicios mensuales',
            },
        ),
    ]
