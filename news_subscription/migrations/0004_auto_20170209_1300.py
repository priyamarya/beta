# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_subscription', '0003_auto_20170115_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='sub_paper',
            field=models.ManyToManyField(to='newspapers.Newspapers', verbose_name='subscribed_for'),
        ),
    ]