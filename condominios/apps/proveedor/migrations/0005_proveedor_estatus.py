# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0004_remove_proveedor_estatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
