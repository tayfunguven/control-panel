# Generated by Django 3.1.7 on 2021-09-22 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0015_auto_20210922_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdeal',
            name='is_displayed',
            field=models.BooleanField(default=False, verbose_name='Gösterim Durumu'),
        ),
    ]
