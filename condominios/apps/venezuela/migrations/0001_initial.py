# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('ciudad', models.CharField(max_length=100)),
                ('capital', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
                'verbose_name': 'Ciudad',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=50)),
                ('iso_3166_2', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Estados',
                'verbose_name': 'Estado',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('municipio', models.CharField(max_length=100)),
                ('estado', models.ForeignKey(to='venezuela.Estado')),
            ],
            options={
                'verbose_name_plural': 'Municipios',
                'verbose_name': 'Municipio',
            },
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('parroquia', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(to='venezuela.Municipio')),
            ],
            options={
                'verbose_name_plural': 'Parroquías',
                'verbose_name': 'Parroquía',
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(to='venezuela.Estado'),
        ),
    ]
