# Generated by Django 3.1.7 on 2021-08-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productregistration',
            name='product_category',
            field=models.CharField(choices=[('Aviwest', 'Aviwest'), ('Electronic Components', 'Electronic Component(Electronik Bileşen)'), ('Broadcast', 'Broadcast(Yayın)'), ('Camera', 'Camera(Kamera)'), ('Decoration', 'Decoration(Dekorasyon)'), ('Computer', 'Computer(Bilgisayar)'), ('Card', 'Card(Kart)'), ('Network', 'Network(Ağ)'), ('Audio', 'Audio(Ses)'), ('Power', 'Power(Güç)'), ('HPA', 'HPA'), ('RF Component', 'RF Component(RF Bileşen)'), ('Monitor', 'Monitor(Monitör)'), ('Accessories', 'Accessories(Aksesuar)'), ('Test Product', 'Test Product(Test Ürünü)'), ('Light', 'Light(Işık)'), ('Scrap', 'Scrap(Hurda)'), ('Demo', 'Demo'), ('Fixture', 'Momento Media Fixture(Demirbaş)')], max_length=25, verbose_name='Kategori'),
        ),
    ]
