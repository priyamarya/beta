# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 15:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0002_subscription_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateTimeField(max_length=8),
        ),
    ]
