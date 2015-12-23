# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0003_prefijocelular'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prefijocelular',
            options={'verbose_name': 'Prefijo celular', 'verbose_name_plural': 'Prefijos celulares'},
        ),
    ]
