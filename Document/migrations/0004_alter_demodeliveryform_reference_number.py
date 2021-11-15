# Generated by Django 3.2.9 on 2021-11-15 13:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Document', '0003_alter_demodeliveryform_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demodeliveryform',
            name='reference_number',
            field=models.CharField(help_text="Referans numarasini 'MM(ADINIZ)-(6 HANELI TARIH)-(BELGE NO)' seklinde giriniz.", max_length=20, validators=[django.core.validators.RegexValidator(message='Girmis oldugunuz referans numarasi uygun formatta degildir! (Ornek format: MMTYFN-010121-001)', regex='^MM[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$')], verbose_name='Referans Numarasi'),
        ),
    ]
