# Generated by Django 3.1.7 on 2021-09-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProductSystem', '0004_auto_20210901_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='productidentification',
            name='images',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='identification_images', to='ProductSystem.productidentificationimages', verbose_name='Görseller'),
            preserve_default=False,
        ),
    ]
