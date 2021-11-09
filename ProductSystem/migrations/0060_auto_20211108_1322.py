# Generated by Django 3.2.9 on 2021-11-08 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0059_auto_20211105_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 11, 8), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(blank=True, default=datetime.date(2021, 11, 8), null=True, verbose_name='İşlem Tarihi'),
        ),
    ]
