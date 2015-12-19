# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0004_auto_20151219_1359'),
    ]

    operations = [
        migrations.AddField(
            model_name='condominio',
            name='telefono',
            field=models.CharField(max_length=11, default=None),
            preserve_default=False,
        ),
    ]
