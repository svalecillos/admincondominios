# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0011_auto_20151219_1941'),
        ('servicio', '0005_auto_20151219_1822'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicioespecial',
            name='condominio',
        ),
        migrations.AddField(
            model_name='servicioespecial',
            name='condominio',
            field=models.ManyToManyField(to='condominio.Condominio'),
        ),
        migrations.AlterField(
            model_name='servicioespecial',
            name='servicio_especial',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.RemoveField(
            model_name='serviciomensual',
            name='condominio',
        ),
        migrations.AddField(
            model_name='serviciomensual',
            name='condominio',
            field=models.ManyToManyField(to='condominio.Condominio'),
        ),
        migrations.AlterField(
            model_name='serviciomensual',
            name='servicio_mensual',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
