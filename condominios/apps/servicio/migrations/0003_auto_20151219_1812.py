# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20151219_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicioespecial',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='serviciomensual',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
