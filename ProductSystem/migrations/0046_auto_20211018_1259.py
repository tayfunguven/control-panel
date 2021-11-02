# Generated by Django 3.1.7 on 2021-10-18 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0045_auto_20211015_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 10, 18), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(blank=True, default=datetime.date(2021, 10, 18), null=True, verbose_name='İşlem Tarihi'),
        ),
    ]
