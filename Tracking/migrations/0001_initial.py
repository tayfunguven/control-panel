# Generated by Django 3.2.9 on 2021-12-14 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=100, verbose_name='Kod')),
                ('product_name', models.CharField(max_length=100, verbose_name='Cihaz Adı')),
                ('has_serial', models.BooleanField(default=False, verbose_name='Seri No - Var/Yok')),
                ('product_amount', models.IntegerField(blank=True, default=1, null=True, verbose_name='Miktar')),
                ('serial_number', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Seri No')),
                ('internal_number', models.CharField(max_length=30, verbose_name='Dahili No')),
                ('product_status', models.CharField(choices=[('Arizali', 'Arızalı Ürün'), ('Sifir', 'Sıfır Ürün'), ('İkinci El', 'İkinci El Ürün'), ('İkinci El/Arizali', 'İkinci El/Arızalı Ürün')], max_length=20, verbose_name='Durum')),
                ('product_category', models.CharField(choices=[('Aviwest', 'Aviwest'), ('Electronic Components', 'Electronic Component(Electronik Bileşen)'), ('Broadcast', 'Broadcast(Yayın)'), ('Camera', 'Camera(Kamera)'), ('Decoration', 'Decoration(Dekorasyon)'), ('Computer', 'Computer(Bilgisayar)'), ('Card', 'Card(Kart)'), ('Network', 'Network(Ağ)'), ('Audio', 'Audio(Ses)'), ('Power', 'Power(Güç)'), ('HPA', 'HPA'), ('RF Component', 'RF Component(RF Bileşen)'), ('Monitor', 'Monitor(Monitör)'), ('Accessories', 'Accessories(Aksesuar)'), ('Test Product', 'Test Product(Test Ürünü)'), ('Light', 'Light(Işık)'), ('Scrap', 'Scrap(Hurda)'), ('Demo', 'Demo'), ('Fixture', 'Momento Media Fixture(Demirbaş)')], max_length=25, verbose_name='Kategori')),
                ('tested_status', models.BooleanField(default=False, verbose_name='Test Edildi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Resim')),
            ],
            options={
                'verbose_name': 'Ürün Kaydı',
                'verbose_name_plural': 'Ürün Kayıtları',
            },
        ),
        migrations.CreateModel(
            name='ProductOutlet',
            fields=[
                ('outlet_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Çıkış Kodu')),
                ('selling_price', models.DecimalField(decimal_places=2, help_text='Türk Lirası - ₺', max_digits=20, verbose_name='Fiyat(tl)')),
                ('quantity', models.IntegerField(default=1, verbose_name='Adet')),
                ('date_departure', models.DateTimeField(auto_now_add=True, verbose_name='İşlem Tarihi')),
                ('date_interval', models.IntegerField(default=0, help_text='Gün', verbose_name='Ne Kadar Kaldı')),
                ('reason_departure', models.CharField(choices=[('Selling', 'Selling(Satış)'), ('Reparation', 'Reparation(Onarım)'), ('Konsinye', 'Konsinye')], max_length=25, verbose_name='Çıkış Nedeni')),
                ('company_name', models.CharField(help_text='Cihazın gönderildiği firma', max_length=50, verbose_name='Firma Adı')),
                ('deliverer_name', models.CharField(help_text='Teslimatı yapan aracının adı', max_length=30, verbose_name='İsim')),
                ('deliverer_surname', models.CharField(help_text='Teslimatı yapan aracının soyadı', max_length=30, verbose_name='Soy İsim')),
                ('deliverer_company', models.CharField(help_text='Teslimatı yapan aracının çalıştığı firma', max_length=50, verbose_name='Firma Adı')),
                ('deliverer_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Posta')),
                ('deliverer_phone', models.CharField(max_length=20, verbose_name='Telefon')),
                ('product_fk', models.ForeignKey(help_text="Yeni ürün eklemek için '+'ya basın!", on_delete=django.db.models.deletion.CASCADE, related_name='product_outlet', to='Tracking.productregistration', verbose_name='Ürün Bilgileri')),
            ],
            options={
                'verbose_name': 'Ürün Çıkışı',
                'verbose_name_plural': 'Ürün Çıkışları',
            },
        ),
        migrations.CreateModel(
            name='ProductIdentifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_serial', models.CharField(blank=True, default='', max_length=30, null=True, verbose_name='Seri No')),
                ('additional_internal', models.CharField(blank=True, max_length=30, null=True, verbose_name='Dahili No')),
                ('additional_description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='Tracking.productregistration')),
            ],
            options={
                'verbose_name': 'Ek Numara',
                'verbose_name_plural': 'Ek Numaralar',
            },
        ),
        migrations.CreateModel(
            name='ProductEnrty',
            fields=[
                ('entry_id', models.BigAutoField(primary_key=True, serialize=False, verbose_name='Giriş Kodu')),
                ('purchase_price', models.DecimalField(decimal_places=2, help_text='Türk Lirası - ₺', max_digits=20, verbose_name='Fiyat(tl)')),
                ('quantity', models.IntegerField(default=1, verbose_name='Adet')),
                ('date_arrival', models.DateTimeField(auto_now_add=True, verbose_name='İşlem Tarihi')),
                ('date_interval', models.IntegerField(default=0, help_text='Gün', verbose_name='Ne Kadar Duracak')),
                ('reason_arrival', models.CharField(choices=[('Purchase', 'Purchase(Satın Alma)'), ('Reparation', 'Reparation(Onarım)'), ('Konsinye', 'Konsinye')], max_length=25, verbose_name='Geliş Nedeni')),
                ('company_name', models.CharField(help_text='Cihazın geliş firması', max_length=50, verbose_name='Firma Adı')),
                ('deliverer_name', models.CharField(help_text='Teslimatı yapan aracının adı', max_length=30, verbose_name='İsim')),
                ('deliverer_surname', models.CharField(help_text='Teslimatı yapan aracının soyadı', max_length=30, verbose_name='Soy İsim')),
                ('deliverer_company', models.CharField(help_text='Teslimatı yapan aracının çalıştığı firma', max_length=50, verbose_name='Firma Adı')),
                ('deliverer_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-Posta')),
                ('deliverer_phone', models.CharField(max_length=20, verbose_name='Telefon')),
                ('product_fk', models.ForeignKey(help_text="Yeni ürün eklemek için '+'ya basın!", on_delete=django.db.models.deletion.CASCADE, related_name='product_entry', to='Tracking.productregistration', verbose_name='Ürün Bilgileri')),
            ],
            options={
                'verbose_name': 'Ürün Girişi',
                'verbose_name_plural': 'Ürün Girişleri',
            },
        ),
    ]
