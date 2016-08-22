# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('laboratory', models.CharField(max_length=250, blank=True, null=True)),
                ('presentation', models.CharField(max_length=250, blank=True, null=True)),
                ('active_principle', models.CharField(max_length=250, blank=True, null=True)),
                ('pmc', models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)),
            ],
        ),
    ]
