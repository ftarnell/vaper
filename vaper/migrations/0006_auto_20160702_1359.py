# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaper', '0005_ledger_ledgerentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7),
        ),
    ]
