# Generated by Django 3.1.7 on 2021-10-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0044_auto_20211015_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoutlet',
            name='has_serial',
            field=models.BooleanField(blank=True, verbose_name='Dahili no ile ara'),
        ),
    ]