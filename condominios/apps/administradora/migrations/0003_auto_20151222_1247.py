# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administradora', '0002_auto_20151222_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='costoservicioespecial',
            options={'verbose_name_plural': 'Costo de servicios especiales'},
        ),
        migrations.AlterField(
            model_name='cargoservicioespecial',
            name='monto',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='cargoserviciomensual',
            name='monto',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='costoservicioespecial',
            name='costo',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='costoserviciomensual',
            name='costo',
            field=models.DecimalField(max_digits=10, decimal_places=2),
        ),
    ]
