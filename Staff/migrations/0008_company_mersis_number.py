# Generated by Django 3.1.7 on 2021-10-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0007_auto_20211020_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='mersis_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Mersis No'),
        ),
    ]
