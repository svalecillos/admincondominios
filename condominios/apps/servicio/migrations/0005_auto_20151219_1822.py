# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0004_auto_20151219_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicioespecial',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='serviciomensual',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
