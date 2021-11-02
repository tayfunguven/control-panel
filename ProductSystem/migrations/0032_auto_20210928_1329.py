# Generated by Django 3.1.7 on 2021-09-28 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0031_auto_20210928_1039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productidentification',
            options={'verbose_name': 'Urun', 'verbose_name_plural': 'Urunler'},
        ),
        migrations.RenameField(
            model_name='productidentification',
            old_name='image_tree',
            new_name='image_three',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='warehouse_info',
        ),
        migrations.AddField(
            model_name='inventory',
            name='product_category',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Kategori'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='shelf_info',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Raf Bilgisi'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='shelf_no',
            field=models.CharField(default=1, max_length=20, verbose_name='Raf No'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='shelf_product_x_axis',
            field=models.IntegerField(blank=True, null=True, verbose_name='Sütun (Column)'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='shelf_product_y_axis',
            field=models.IntegerField(blank=True, null=True, verbose_name='Satır (Row)'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='warehouse_location',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Lokasyon'),
        ),
    ]