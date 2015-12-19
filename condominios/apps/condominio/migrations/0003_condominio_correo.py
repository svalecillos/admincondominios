# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0002_auto_20151219_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='correo',
            field=models.EmailField(max_length=254, default='admin@jj.com'),
        ),
    ]
