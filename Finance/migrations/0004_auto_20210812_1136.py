# Generated by Django 3.1.7 on 2021-08-12 08:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Finance', '0003_auto_20210806_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancepayment',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='comission',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='companyexpense',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='companyincome',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='incentive',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='personalexpense',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='personalexpenseforuserentry',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='personalincome',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='punishment',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
        migrations.AlterField(
            model_name='salaryinfo',
            name='log_date',
            field=models.DateField(default=datetime.date(2021, 8, 12), verbose_name='İşlem Tarihi'),
        ),
    ]