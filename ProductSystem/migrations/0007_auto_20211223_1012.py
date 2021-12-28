# Generated by Django 3.2.9 on 2021-12-23 07:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0006_auto_20211222_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 12, 23), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(blank=True, default=datetime.date(2021, 12, 23), null=True, verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='rmaproduct',
            name='log_date',
            field=models.DateField(blank=True, default=datetime.date(2021, 12, 23), null=True, verbose_name='İşlem Tarihi'),
        ),
    ]