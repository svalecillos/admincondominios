# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0007_condominio_estatus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='estatus',
            field=models.BooleanField(default=True),
        ),
    ]
