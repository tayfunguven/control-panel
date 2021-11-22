# Generated by Django 3.2.9 on 2021-11-22 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0075_auto_20211122_1257'),
        ('Document', '0009_auto_20211122_1332'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demoproduct',
            options={'verbose_name': 'Demo Ürünleri'},
        ),
        migrations.RemoveField(
            model_name='devicedeliveryform',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='devicedeliveryform',
            name='return_date',
        ),
        migrations.CreateModel(
            name='DeviceDeliveryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demo_duration', models.CharField(max_length=1000, verbose_name='Teslim Süresi')),
                ('quantity', models.CharField(blank=True, max_length=100, null=True, verbose_name='Adet')),
                ('form_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Document.devicedeliveryform', verbose_name='Form Id')),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProductSystem.inventory', verbose_name='Ürün Adi')),
                ('product_specifications', models.ManyToManyField(to='ProductSystem.ProductIdentification', verbose_name='Bilgiler')),
            ],
            options={
                'verbose_name': 'Cihaz Teslim Ürünleri',
            },
        ),
    ]
