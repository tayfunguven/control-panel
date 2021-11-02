# Generated by Django 3.1.7 on 2021-09-20 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0017_auto_20210920_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorycard',
            name='product_code',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ürün Kodu'),
        ),
        migrations.AlterField(
            model_name='inventorycard',
            name='product_name',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ürün Adı'),
        ),
    ]