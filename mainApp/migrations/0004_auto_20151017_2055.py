# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20151017_2001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propositoparticular',
            name='usuario',
        ),
        migrations.AddField(
            model_name='userperfil',
            name='adquirir',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userperfil',
            name='liberar',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='userperfil',
            name='reafirmar',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='PropositoParticular',
        ),
    ]
