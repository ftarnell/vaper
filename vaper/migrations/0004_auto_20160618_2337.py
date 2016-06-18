# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 23:37
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaper', '0003_remove_flavour_ml_remaining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flavour',
            name='ml',
            field=models.DecimalField(decimal_places=2, max_digits=7, validators=[django.core.validators.MinValueValidator(0)], verbose_name=b'Remaining (ml)'),
        ),
        migrations.AlterField(
            model_name='flavourinstance',
            name='strength',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
