# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pagos', '0001_initial'),
        ('venezuela', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registropago',
            name='banco',
            field=models.ForeignKey(to='venezuela.Banco'),
        ),
        migrations.AddField(
            model_name='registropago',
            name='pagadoPor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='registropago',
            name='tipoDePago',
            field=models.ForeignKey(to='pagos.TipoDePago'),
        ),
    ]
