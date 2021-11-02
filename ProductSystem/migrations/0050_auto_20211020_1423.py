# Generated by Django 3.1.7 on 2021-10-20 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GeneralModel', '0004_deliverycompany'),
        ('ProductSystem', '0049_auto_20211020_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productenrty',
            name='delivery_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_delivery_companies', to='GeneralModel.deliverycompany', verbose_name='Kargo Firmasi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='delivery_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outlet_delivery_companies', to='GeneralModel.deliverycompany', verbose_name='Kargo Firmasi'),
        ),
        migrations.DeleteModel(
            name='DeliveryCompany',
        ),
    ]
