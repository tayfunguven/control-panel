# Generated by Django 3.1.7 on 2021-09-02 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0005_auto_20210901_1448'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerProjectSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Proje',
                'verbose_name_plural': 'Projeler',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('ProjectForm.registerlogs',),
        ),
        migrations.AlterField(
            model_name='registerdeal',
            name='project_date',
            field=models.DateField(default=datetime.date(2021, 9, 2), verbose_name='Proje Tarihi'),
        ),
    ]