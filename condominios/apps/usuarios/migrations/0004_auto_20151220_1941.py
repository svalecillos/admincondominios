# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_auto_20151025_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='telefono_habitacion',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='telefono_movil',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
