# Generated by Django 3.2.8 on 2021-11-01 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0034_alter_registerdeal_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 11, 1), verbose_name='Proje Tarihi'),
        ),
    ]
