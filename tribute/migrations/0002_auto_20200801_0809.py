# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-01 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tribute', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='memories',
            field=models.CharField(choices=[('memories', 'Memories'), ('tributes', 'Tributes')], default='memories', max_length=10),
        ),
    ]
