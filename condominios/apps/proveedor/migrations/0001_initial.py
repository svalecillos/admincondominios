# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('condominio', '0006_auto_20151219_1531'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('proveedor', models.CharField(max_length=100)),
                ('rif', models.CharField(max_length=13)),
                ('estatus', models.BooleanField()),
                ('condominio', models.ForeignKey(to='condominio.Condominio')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
    ]
