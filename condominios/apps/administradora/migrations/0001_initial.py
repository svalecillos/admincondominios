# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0005_auto_20151221_2106'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CargoServicioEspecial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Cargo servicios especiales',
            },
        ),
        migrations.CreateModel(
            name='CargoServicioMensual',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('monto', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fecha', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Cargo servicios mensuales',
            },
        ),
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('condominio', models.CharField(max_length=100, unique=True)),
                ('rif', models.CharField(max_length=13, null=True, blank=True)),
                ('telefono', models.CharField(max_length=12, default='', null=True)),
                ('correo', models.EmailField(max_length=254, null=True)),
                ('avenidaCalle', models.CharField(max_length=150)),
                ('urbanizacionSector', models.CharField(max_length=80)),
                ('nombreEdificacion', models.CharField(max_length=150, null=True)),
                ('estatus', models.BooleanField(default=True)),
                ('ciudad', models.ForeignKey(to='venezuela.Ciudad')),
                ('creadorPor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('parroquia', models.ForeignKey(to='venezuela.Parroquia')),
            ],
            options={
                'verbose_name_plural': 'Condominios',
            },
        ),
        migrations.CreateModel(
            name='CostoServicioEspecial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(max_digits=10, decimal_places=5)),
                ('cuota', models.PositiveSmallIntegerField()),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('condominio', models.ForeignKey(to='administradora.Condominio')),
            ],
            options={
                'verbose_name_plural': 'Costo de servicio especiales',
            },
        ),
        migrations.CreateModel(
            name='CostoServicioMensual',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('costo', models.DecimalField(max_digits=10, decimal_places=5)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('condominio', models.ForeignKey(to='administradora.Condominio')),
            ],
            options={
                'verbose_name_plural': 'Costo de servicio mensuales',
            },
        ),
        migrations.CreateModel(
            name='CuentaCondominio',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('condominio', models.OneToOneField(to='administradora.Condominio')),
            ],
            options={
                'verbose_name_plural': 'Cuenta de condominios',
            },
        ),
        migrations.CreateModel(
            name='CuentaUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(max_digits=10, decimal_places=2)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cuenta de usuarios',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('proveedor', models.CharField(max_length=100)),
                ('rif', models.CharField(max_length=13, null=True, blank=True)),
                ('telefono', models.CharField(max_length=12, null=True)),
                ('correo', models.EmailField(max_length=254, null=True)),
                ('condominio', models.ForeignKey(to='administradora.Condominio')),
                ('creadoPor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='ServicioEspecial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('servicioEspecial', models.CharField(max_length=50, null=True)),
                ('estatus', models.BooleanField(default=True)),
                ('condominio', models.ForeignKey(to='administradora.Condominio')),
                ('proveedor', models.ForeignKey(to='administradora.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Servicios especiales',
            },
        ),
        migrations.CreateModel(
            name='ServicioMensual',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('servicioMensual', models.CharField(max_length=50, null=True)),
                ('estatus', models.BooleanField(default=True)),
                ('condominio', models.ForeignKey(to='administradora.Condominio')),
                ('proveedor', models.ForeignKey(to='administradora.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Servicios mensuales',
            },
        ),
        migrations.CreateModel(
            name='TipoEdificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('edificacion', models.CharField(max_length=80)),
                ('estatus', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Edificaciones',
            },
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('debito', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=5)),
                ('credito', models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=5)),
                ('descripcion', models.CharField(max_length=80)),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('aprobado', models.BooleanField(default=True)),
                ('CuentaCondominio', models.ForeignKey(to='administradora.CuentaCondominio')),
                ('CuentaUsuario', models.ForeignKey(to='administradora.CuentaUsuario')),
            ],
            options={
                'verbose_name_plural': 'Transacciones',
            },
        ),
        migrations.AddField(
            model_name='costoserviciomensual',
            name='servicioMensual',
            field=models.ForeignKey(to='administradora.ServicioMensual'),
        ),
        migrations.AddField(
            model_name='costoservicioespecial',
            name='servicioEspecial',
            field=models.ForeignKey(to='administradora.ServicioEspecial'),
        ),
        migrations.AddField(
            model_name='condominio',
            name='tipoEdificacion',
            field=models.ForeignKey(to='administradora.TipoEdificacion', null=True),
        ),
        migrations.AddField(
            model_name='cargoserviciomensual',
            name='condominio',
            field=models.ForeignKey(to='administradora.Condominio'),
        ),
        migrations.AddField(
            model_name='cargoserviciomensual',
            name='creadorPor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargoserviciomensual',
            name='proveedor',
            field=models.ForeignKey(to='administradora.Proveedor'),
        ),
        migrations.AddField(
            model_name='cargoserviciomensual',
            name='servicioMensual',
            field=models.ForeignKey(to='administradora.ServicioMensual'),
        ),
        migrations.AddField(
            model_name='cargoservicioespecial',
            name='condominio',
            field=models.ForeignKey(to='administradora.Condominio'),
        ),
        migrations.AddField(
            model_name='cargoservicioespecial',
            name='creadorPor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cargoservicioespecial',
            name='proveedor',
            field=models.ForeignKey(to='administradora.Proveedor'),
        ),
        migrations.AddField(
            model_name='cargoservicioespecial',
            name='servicioEspecial',
            field=models.ForeignKey(to='administradora.ServicioEspecial'),
        ),
    ]
