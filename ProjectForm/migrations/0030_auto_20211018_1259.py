# Generated by Django 3.1.7 on 2021-10-18 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0029_auto_20211015_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 10, 18), verbose_name='Proje Tarihi'),
        ),
    ]