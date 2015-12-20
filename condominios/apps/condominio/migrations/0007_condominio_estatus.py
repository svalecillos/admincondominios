# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0006_auto_20151219_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='estatus',
            field=models.BooleanField(default=None),
            preserve_default=False,
        ),
    ]
