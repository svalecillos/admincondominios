# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0002_auto_20151219_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
