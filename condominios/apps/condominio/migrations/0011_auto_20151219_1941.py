# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0010_condominio_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='ciudad',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='condominio',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='correo',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='condominio',
            name='telefono',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
