# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 13:38
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, default=9834598345, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\d{9,10}$')]),
            preserve_default=False,
        ),
    ]
