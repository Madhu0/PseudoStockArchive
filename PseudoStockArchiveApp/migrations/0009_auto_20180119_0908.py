# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-19 09:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PseudoStockArchiveApp', '0008_auto_20180119_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradingdata',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 1, 19, 9, 8, 21, 354190, tzinfo=utc)),
        ),
    ]