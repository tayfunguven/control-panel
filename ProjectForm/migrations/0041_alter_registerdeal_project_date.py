# Generated by Django 3.2.9 on 2021-11-09 08:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0040_alter_registerdeal_project_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 11, 9), verbose_name='Proje Tarihi'),
        ),
    ]