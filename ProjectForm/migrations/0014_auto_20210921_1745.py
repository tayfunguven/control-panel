# Generated by Django 3.1.7 on 2021-09-21 14:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0013_auto_20210920_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 9, 21), verbose_name='Proje Tarihi'),
        ),
    ]
