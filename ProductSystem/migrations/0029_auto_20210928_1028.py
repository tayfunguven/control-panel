# Generated by Django 3.1.7 on 2021-09-28 07:28

import ProductSystem.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0028_auto_20210928_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='productoutlet',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=ProductSystem.models.ProductOutlet.user_directory_path, verbose_name='Görsel 2'),
        ),
        migrations.AddField(
            model_name='productoutlet',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=ProductSystem.models.ProductOutlet.user_directory_path, verbose_name='Görsel 3'),
        ),
        migrations.AddField(
            model_name='productoutlet',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=ProductSystem.models.ProductOutlet.user_directory_path, verbose_name='Görsel 4'),
        ),
    ]
