# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('usuario', models.CharField(unique=True, max_length=50)),
                ('cedula', models.PositiveIntegerField(max_length=8)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('numero_vivienda', models.CharField(max_length=5)),
                ('activo', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(verbose_name='groups', related_name='user_set', blank=True, to='auth.Group', help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', related_name='user_set', blank=True, to='auth.Permission', help_text='Specific permissions for this user.', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
