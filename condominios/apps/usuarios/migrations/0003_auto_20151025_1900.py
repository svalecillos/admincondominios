# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_auto_20151025_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='activo',
            new_name='is_active',
        ),
        migrations.AddField(
            model_name='usuario',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
