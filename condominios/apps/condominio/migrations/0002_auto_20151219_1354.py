# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='condominio',
            options={'verbose_name_plural': 'Condominios'},
        ),
    ]
