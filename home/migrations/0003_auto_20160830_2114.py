# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-30 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20160828_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projecto',
            name='descripcion',
            field=models.TextField(blank=True, max_length=1500),
        ),
    ]
