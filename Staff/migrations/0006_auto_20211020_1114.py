# Generated by Django 3.1.7 on 2021-10-20 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0005_auto_20211020_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Adres'),
        ),
    ]