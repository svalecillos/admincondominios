# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0005_condominio_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]
