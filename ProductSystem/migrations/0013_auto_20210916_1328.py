# Generated by Django 3.1.7 on 2021-09-16 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0012_auto_20210916_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorycardimageset',
            name='image_four',
            field=models.ImageField(blank=True, null=True, upload_to='stock_card_images/product {InventoryCard.product_code}', verbose_name='Görsel 4'),
        ),
        migrations.AlterField(
            model_name='inventorycardimageset',
            name='image_tree',
            field=models.ImageField(blank=True, null=True, upload_to='stock_card_images/product {InventoryCard.product_code}', verbose_name='Görsel 3'),
        ),
        migrations.AlterField(
            model_name='inventorycardimageset',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='stock_card_images/product {InventoryCard.product_code}', verbose_name='Görsel 2'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='deliverer',
            field=models.ManyToManyField(blank=True, null=True, related_name='entry_deliverers', to='ProductSystem.Deliverer', verbose_name='Teslimat Yapan Kişi'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='delivery_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_delivery_companies', to='ProductSystem.deliverycompany', verbose_name='Teslimat Yapan Firma'),
        ),
    ]
