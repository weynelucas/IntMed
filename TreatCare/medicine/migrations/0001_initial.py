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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=250)),
                ('laboratory', models.CharField(null=True, blank=True, max_length=250)),
                ('presentation', models.CharField(null=True, blank=True, max_length=250)),
                ('active_principle', models.CharField(null=True, blank=True, max_length=250)),
                ('pmc', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=10)),
            ],
        ),
    ]
