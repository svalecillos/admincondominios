# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0004_auto_20151221_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefijocelular',
            name='prefijo',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='prefijotelefonico',
            name='prefijo',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
