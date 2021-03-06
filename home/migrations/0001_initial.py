# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 23:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImagenesProjectos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='projectos')),
                ('principal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Projecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('descripcion', models.TextField(blank=True, max_length=250)),
                ('estatus', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='imagenesprojectos',
            name='projecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Projecto'),
        ),
    ]
