# Generated by Django 3.1.7 on 2021-10-20 08:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0004_auto_20211020_1104'),
        ('ProductSystem', '0047_auto_20211019_0940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyauthorizedperson',
            name='company_id',
        ),
        migrations.RemoveField(
            model_name='deliverer',
            name='delivery_company',
        ),
        migrations.RenameField(
            model_name='deliverycompany',
            old_name='name',
            new_name='cargo_name',
        ),
        migrations.RemoveField(
            model_name='deliverycompany',
            name='cargo_code',
        ),
        migrations.RemoveField(
            model_name='productenrty',
            name='deliverer',
        ),
        migrations.RemoveField(
            model_name='productoutlet',
            name='deliverer',
        ),
        migrations.AddField(
            model_name='deliverycompany',
            name='cargo_branch',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Teslimat Subesi'),
        ),
        migrations.AddField(
            model_name='productenrty',
            name='delivery_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Teslimat Kodu'),
        ),
        migrations.AddField(
            model_name='productenrty',
            name='delivery_warehouse_receipt_document',
            field=models.FileField(blank=True, null=True, upload_to='ProductSystem/DeliveryDocs/', verbose_name='Ambar Tesellum Fisi'),
        ),
        migrations.AddField(
            model_name='productoutlet',
            name='delivery_code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Teslimat Kodu'),
        ),
        migrations.AddField(
            model_name='productoutlet',
            name='delivery_warehouse_receipt_document',
            field=models.FileField(blank=True, null=True, upload_to='ProductSystem/DeliveryDocs/', verbose_name='Ambar Tesellum Fisi'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_companies', to='Staff.company', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='company_authorized',
            field=models.ManyToManyField(blank=True, null=True, related_name='entry_company_authorizeds', to='Staff.CompanyAuthorizedPerson', verbose_name='Firma Yetkilisi'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='date_arrival',
            field=models.DateField(default=datetime.date(2021, 10, 20), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productenrty',
            name='delivery_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_delivery_companies', to='ProductSystem.deliverycompany', verbose_name='Kargo Firmasi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outlet_companies', to='Staff.company', verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='company_authorized',
            field=models.ManyToManyField(blank=True, null=True, related_name='outlet_company_authorizeds', to='Staff.CompanyAuthorizedPerson', verbose_name='Firma Yetkilisi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='date_departure',
            field=models.DateField(blank=True, default=datetime.date(2021, 10, 20), null=True, verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='productoutlet',
            name='delivery_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='outlet_delivery_companies', to='ProductSystem.deliverycompany', verbose_name='Kargo Firmasi'),
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='CompanyAuthorizedPerson',
        ),
        migrations.DeleteModel(
            name='Deliverer',
        ),
    ]
