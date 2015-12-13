# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion_estado',
            name='nombre',
            field=models.CharField(unique=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion_municipio',
            name='nombre',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='direccion_parroquia',
            name='nombre',
            field=models.CharField(unique=True, max_length=30),
        ),
    ]
