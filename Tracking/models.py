from django.db import models
from datetime import datetime

PRODUCT_STATUS = [
    ('Arizali','Arızalı Ürün'),
    ('Sifir', 'Sıfır Ürün'),
    ('İkinci El', 'İkinci El Ürün'),
    ('İkinci El/Arizali', 'İkinci El/Arızalı Ürün')
]
CATEGORIES = [
    ('Aviwest','Aviwest'),
    ('Electronic Components', 'Electronic Component(Electronik Bileşen)'),
    ('Broadcast','Broadcast(Yayın)'),
    ('Camera','Camera(Kamera)'),
    ('Decoration','Decoration(Dekorasyon)'),
    ('Computer','Computer(Bilgisayar)'),
    ('Card','Card(Kart)'),
    ('Network','Network(Ağ)'),
    ('Audio','Audio(Ses)'),
    ('Power','Power(Güç)'),
    ('HPA','HPA'),
    ('RF Component','RF Component(RF Bileşen)'),
    ('Monitor','Monitor(Monitör)'),
    ('Accessories','Accessories(Aksesuar)'),
    ('Test Product','Test Product(Test Ürünü)'),
    ('Light','Light(Işık)'),
    ('Scrap','Scrap(Hurda)'),
    ('Demo', 'Demo'),
    ('Fixture', 'Momento Media Fixture(Demirbaş)')
]

REASON_ARRIVAL = [
    ('Purchase','Purchase(Satın Alma)'),
    ('Reparation','Reparation(Onarım)'),
    ('Konsinye','Konsinye'),
]

REASON_DEPARTURE = [
    ('Selling','Selling(Satış)'),
    ('Reparation','Reparation(Onarım)'),
    ('Konsinye','Konsinye'),
]

class ProductRegistration(models.Model):
    product_id = models.CharField("Kod", max_length=100, unique=False)
    product_name = models.CharField("Cihaz Adı", max_length=100)
    has_serial = models.BooleanField("Seri No - Var/Yok", default=False)
    product_amount = models.IntegerField("Miktar", default=1, blank=True,null=True)
    serial_number = models.CharField("Seri No",unique=False,default='', blank=True,null=True, max_length=30)
    internal_number = models.CharField("Dahili No",unique=False, max_length=30)
    product_status = models.CharField("Durum", max_length=20, choices=PRODUCT_STATUS)
    product_category = models.CharField("Kategori", max_length=25, choices=CATEGORIES)
    tested_status = models.BooleanField("Test Edildi", default=False)
    description = models.TextField("Açıklama", blank=True, null=True)
    photo = models.ImageField("Resim",upload_to='products', blank=True, null=True)
    
    
    def __str__(self):
        return "Ürün Kodu = " + str(self.product_id)

    class Meta:
        verbose_name = ("Ürün Kaydı")
        verbose_name_plural = ("Ürün Kayıtları")
        
class ProductIdentifications(models.Model):
    additional_serial = models.CharField("Seri No",unique=False,default='', blank=True,null=True, max_length=30)
    additional_internal = models.CharField("Dahili No",unique=False, blank=True, null=True, max_length=30)
    additional_description = models.TextField("Açıklama", blank=True, null=True)
    product_id = models.ForeignKey(ProductRegistration, related_name="children", on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Ek Numara")
        verbose_name_plural = ("Ek Numaralar")
        
        
class ProductEnrty(models.Model):
    entry_id = models.BigAutoField(primary_key=True, verbose_name="Giriş Kodu")
    purchase_price = models.DecimalField("Fiyat(tl)", help_text="Türk Lirası - ₺", blank=False, null=False, max_digits=20, decimal_places=2)
    quantity = models.IntegerField("Adet", blank=False, null=False, default=1)
    date_arrival = models.DateTimeField("İşlem Tarihi", auto_now_add=True)
    date_interval = models.IntegerField("Ne Kadar Duracak", help_text="Gün", default=0)
    reason_arrival = models.CharField("Geliş Nedeni", max_length=25, choices=REASON_ARRIVAL)
    product_fk = models.ForeignKey(ProductRegistration, help_text="Yeni ürün eklemek için '+'ya basın!", related_name="product_entry", on_delete=models.CASCADE, verbose_name="Ürün Bilgileri")
    company_name = models.CharField("Firma Adı", help_text="Cihazın geliş firması", max_length=50, blank=False, null=False)
    deliverer_name = models.CharField("İsim", help_text="Teslimatı yapan aracının adı", max_length=30, blank=False, null=False)
    deliverer_surname = models.CharField("Soy İsim", help_text="Teslimatı yapan aracının soyadı", max_length=30, blank=False, null=False)
    deliverer_company = models.CharField("Firma Adı", help_text="Teslimatı yapan aracının çalıştığı firma", max_length=50, blank=False, null=False)
    deliverer_email = models.EmailField("E-Posta", blank=True, null=True)
    deliverer_phone = models.CharField("Telefon", max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.entry_id)

    class Meta:
        verbose_name = ("Ürün Girişi")
        verbose_name_plural = ("Ürün Girişleri")

class ProductOutlet(models.Model):
    outlet_id = models.BigAutoField(primary_key=True, verbose_name="Çıkış Kodu")
    selling_price = models.DecimalField("Fiyat(tl)", help_text="Türk Lirası - ₺", blank=False, null=False, max_digits=20, decimal_places=2)
    quantity = models.IntegerField("Adet", blank=False, null=False, default=1)
    date_departure = models.DateTimeField("İşlem Tarihi", auto_now_add=True)
    date_interval = models.IntegerField("Ne Kadar Kaldı", help_text="Gün", default=0)
    reason_departure = models.CharField("Çıkış Nedeni", max_length=25, choices=REASON_DEPARTURE)
    product_fk = models.ForeignKey(ProductRegistration, help_text="Yeni ürün eklemek için '+'ya basın!", related_name="product_outlet", on_delete=models.CASCADE, verbose_name="Ürün Bilgileri")
    company_name = models.CharField("Firma Adı", help_text="Cihazın gönderildiği firma", max_length=50, blank=False, null=False)
    deliverer_name = models.CharField("İsim", help_text="Teslimatı yapan aracının adı", max_length=30, blank=False, null=False)
    deliverer_surname = models.CharField("Soy İsim", help_text="Teslimatı yapan aracının soyadı", max_length=30, blank=False, null=False)
    deliverer_company = models.CharField("Firma Adı", help_text="Teslimatı yapan aracının çalıştığı firma", max_length=50, blank=False, null=False)
    deliverer_email = models.EmailField("E-Posta", blank=True, null=True)
    deliverer_phone = models.CharField("Telefon", max_length=20, blank=False, null=False)
    
    def __str__(self):
        return str(self.outlet_id)

    class Meta:
        verbose_name = ("Ürün Çıkışı")
        verbose_name_plural = ("Ürün Çıkışları")
    