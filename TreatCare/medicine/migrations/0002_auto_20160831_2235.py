# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-01 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicine',
            options={'verbose_name': 'medicamento', 'verbose_name_plural': 'medicamentos'},
        ),
    ]
