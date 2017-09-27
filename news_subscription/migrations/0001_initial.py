# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newspapers', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_paper', models.ManyToManyField(to='newspapers.Newspapers', verbose_name='subscribed for')),
                ('sub_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sub_by_user', to='users.Users', verbose_name='subscriber')),
            ],
            options={
                'verbose_name': ' Subscriptions',
                'verbose_name_plural': 'Subscriptions',
            },
        ),
    ]
