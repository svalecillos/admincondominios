# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedor', '0003_auto_20151219_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proveedor',
            name='estatus',
        ),
    ]
