# Generated by Django 3.1.7 on 2021-09-21 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0018_auto_20210920_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='product_code',
            field=models.CharField(max_length=200, verbose_name='Kod'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='product_name',
            field=models.CharField(max_length=1000, verbose_name='Cihaz Adı'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 9, 21), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(default=datetime.date(2021, 9, 21), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='warehouseinfo',
            name='shelf_product_x_axis',
            field=models.IntegerField(verbose_name='Sütun (Column)'),
        ),
        migrations.AlterField(
            model_name='warehouseinfo',
            name='shelf_product_y_axis',
            field=models.IntegerField(verbose_name='Satır (Row)'),
        ),
    ]