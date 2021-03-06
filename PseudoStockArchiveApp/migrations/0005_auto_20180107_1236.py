# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-07 12:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PseudoStockArchiveApp', '0004_auto_20180107_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='marketCap',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=25),
        ),
        migrations.AlterField(
            model_name='tradingdata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 7, 12, 36, 29, 289795, tzinfo=utc)),
        ),
    ]
