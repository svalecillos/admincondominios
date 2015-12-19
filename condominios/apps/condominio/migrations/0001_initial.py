# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('condominio', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('urbanizacion_sector', models.CharField(max_length=80)),
                ('avenida_calle', models.CharField(max_length=150)),
                ('parroquia', models.ForeignKey(to='venezuela.Parroquia')),
            ],
            options={
                'verbose_name_plural': 'MODELNAMEs',
                'verbose_name': 'MODELNAME',
            },
        ),
    ]
