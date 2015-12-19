# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0003_condominio_correo'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='nombre_edificacion',
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='condominio',
            name='correo',
            field=models.EmailField(max_length=254),
        ),
    ]
