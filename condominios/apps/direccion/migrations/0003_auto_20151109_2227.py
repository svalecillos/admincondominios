# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direccion', '0002_auto_20151107_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='Municipios',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('municipio', models.CharField(unique=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Parroquias',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('parroquia', models.CharField(unique=True, max_length=30)),
                ('municipio', models.ForeignKey(to='direccion.Municipios')),
            ],
        ),
        migrations.RenameModel(
            old_name='direccion_estado',
            new_name='Estados',
        ),
        migrations.RemoveField(
            model_name='direccion_municipio',
            name='estado_id',
        ),
        migrations.RemoveField(
            model_name='direccion_parroquia',
            name='estado_id',
        ),
        migrations.RemoveField(
            model_name='direccion_parroquia',
            name='municipio_id',
        ),
        migrations.RenameField(
            model_name='estados',
            old_name='nombre',
            new_name='estado',
        ),
        migrations.DeleteModel(
            name='direccion_municipio',
        ),
        migrations.DeleteModel(
            name='direccion_parroquia',
        ),
        migrations.AddField(
            model_name='municipios',
            name='estado',
            field=models.ForeignKey(to='direccion.Estados'),
        ),
    ]
