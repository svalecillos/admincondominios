# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venezuela', '0002_prefijotelefonico'),
    ]

    operations = [
        migrations.CreateModel(
            name='prefijoCelular',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('prefijo', models.PositiveSmallIntegerField(max_length=4)),
            ],
            options={
                'verbose_name_plural': 'Prefijos tcelular',
                'verbose_name': 'Prefijo celular',
            },
        ),
    ]
