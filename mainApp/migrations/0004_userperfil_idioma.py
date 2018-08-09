# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20151101_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='userperfil',
            name='idioma',
            field=models.CharField(default=b'es', max_length=100, null=True, blank=True),
        ),
    ]
