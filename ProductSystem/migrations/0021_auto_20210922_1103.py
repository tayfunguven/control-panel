# Generated by Django 3.1.7 on 2021-09-22 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0020_auto_20210922_1019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productidentification',
            name='images',
        ),
        migrations.AddField(
            model_name='productidentification',
            name='image_four',
            field=models.ImageField(blank=True, null=True, upload_to='InventoryCard/Images', verbose_name='Görsel 4'),
        ),
        migrations.AddField(
            model_name='productidentification',
            name='image_one',
            field=models.ImageField(blank=True, null=True, upload_to='InventoryCard/Images', verbose_name='Görsel 1'),
        ),
        migrations.AddField(
            model_name='productidentification',
            name='image_tree',
            field=models.ImageField(blank=True, null=True, upload_to='InventoryCard/Images', verbose_name='Görsel 3'),
        ),
        migrations.AddField(
            model_name='productidentification',
            name='image_two',
            field=models.ImageField(blank=True, null=True, upload_to='InventoryCard/Images', verbose_name='Görsel 2'),
        ),
    ]
