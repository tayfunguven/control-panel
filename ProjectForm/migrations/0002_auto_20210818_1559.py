# Generated by Django 3.1.7 on 2021-08-18 12:59

import ProjectForm.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registerdeal',
            options={'verbose_name': 'Proje Kaydı', 'verbose_name_plural': 'Proje Kayıtları'},
        ),
        migrations.AlterField(
            model_name='registerdeal',
            name='deal_id',
            field=models.BigAutoField(primary_key=True, serialize=False, verbose_name='Proje ID'),
        ),
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 8, 18), validators=[ProjectForm.models.RegisterDeal.validate_initial_date], verbose_name='Proje Tarihi'),
        ),
    ]