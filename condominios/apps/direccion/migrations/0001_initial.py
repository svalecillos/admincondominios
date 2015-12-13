# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='direccion_estado',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='direccion_municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True)),
                ('estado_id', models.ForeignKey(to='direccion.direccion_estado')),
            ],
        ),
        migrations.CreateModel(
            name='direccion_parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15, unique=True)),
                ('estado_id', models.ForeignKey(to='direccion.direccion_estado')),
                ('municipio_id', models.ForeignKey(to='direccion.direccion_municipio')),
            ],
        ),
    ]
