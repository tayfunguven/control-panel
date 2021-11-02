# Generated by Django 3.1.7 on 2021-09-10 11:00

import ProductSystem.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0008_auto_20210910_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!", regex='^\\+?1?\\d{9,13}$')], verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='companyauthorizedperson',
            name='phone',
            field=models.CharField(max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!", regex='^\\+?1?\\d{9,13}$')], verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='deliverer',
            name='phone',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!", regex='^\\+?1?\\d{9,13}$')], verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='image',
            field=models.ImageField(upload_to=ProductSystem.models.ProductEnrty.user_directory_path, verbose_name='Görsel'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='image',
            field=models.ImageField(upload_to=ProductSystem.models.ProductOutlet.user_directory_path, verbose_name='Görsel'),
        ),
    ]