# Generated by Django 3.1.7 on 2021-10-15 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0028_auto_20211007_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 10, 15), verbose_name='Proje Tarihi'),
        ),
    ]