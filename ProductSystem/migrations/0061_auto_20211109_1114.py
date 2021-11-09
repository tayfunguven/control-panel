# Generated by Django 3.2.9 on 2021-11-09 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0060_auto_20211108_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 11, 9), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(blank=True, default=datetime.date(2021, 11, 9), null=True, verbose_name='İşlem Tarihi'),
        ),
    ]