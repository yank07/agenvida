# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.DateField()),
                ('cumplimiento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proposito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes_ano', models.DateField()),
                ('proposito', models.TextField()),
                ('usuario', models.ForeignKey(related_name='propositos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_marcacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50)),
                ('RangoSup', models.IntegerField()),
                ('RangoInf', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPerfil',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pais', models.CharField(max_length=100, null=True, blank=True)),
                ('nacimiento', models.DateField(null=True, blank=True)),
                ('ideal_personal', models.TextField(null=True, blank=True)),
                ('reafirmar', models.TextField(null=True, blank=True)),
                ('liberar', models.TextField(null=True, blank=True)),
                ('adquirir', models.TextField(null=True, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vinculacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vinculacion', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='proposito',
            name='vinculacion',
            field=models.ForeignKey(related_name='propositos', blank=True, to='mainApp.Vinculacion', null=True),
        ),
        migrations.AddField(
            model_name='marcacion',
            name='proposito',
            field=models.ForeignKey(related_name='marcaciones', to='mainApp.Proposito'),
        ),
        migrations.AddField(
            model_name='marcacion',
            name='usuario',
            field=models.ForeignKey(related_name='marcaciones', to=settings.AUTH_USER_MODEL),
        ),
    ]
