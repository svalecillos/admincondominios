# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrefijoTelefonico',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('prefijo', models.PositiveSmallIntegerField(max_length=4)),
                ('municipio', models.ForeignKey(to='venezuela.Municipio')),
            ],
            options={
                'verbose_name': 'Prefijo telefonico',
                'verbose_name_plural': 'Prefijos telefonicos',
            },
        ),
    ]
