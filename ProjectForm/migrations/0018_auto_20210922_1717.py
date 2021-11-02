# Generated by Django 3.1.7 on 2021-09-22 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectForm', '0017_auto_20210922_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerdeal',
            name='is_displayed',
            field=models.BooleanField(default=False, verbose_name='Herkese açık olarak gösterilsin mi?'),
        ),
        migrations.AlterField(
            model_name='registerlogs',
            name='is_displayed',
            field=models.BooleanField(editable=False, verbose_name='Herkese açık olarak gösterilsin mi?'),
        ),
    ]