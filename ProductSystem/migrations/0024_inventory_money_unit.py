# Generated by Django 3.1.7 on 2021-09-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0023_inventory_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='money_unit',
            field=models.CharField(choices=[('TRY', 'TRY'), ('USD', 'USD'), ('EUR', 'EUR')], default='TRY', max_length=10, verbose_name='Para Birimi'),
        ),
    ]
