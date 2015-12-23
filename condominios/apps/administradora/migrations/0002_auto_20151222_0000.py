# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administradora', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargoservicioespecial',
            old_name='creadorPor',
            new_name='creadoPor',
        ),
        migrations.RenameField(
            model_name='cargoserviciomensual',
            old_name='creadorPor',
            new_name='creadoPor',
        ),
        migrations.RenameField(
            model_name='condominio',
            old_name='creadorPor',
            new_name='creadoPor',
        ),
    ]
