# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_userperfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userperfil',
            name='ideal_personal',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userperfil',
            name='nacimiento',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userperfil',
            name='pais',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
