# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_oracion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oracion',
            name='contenido',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
