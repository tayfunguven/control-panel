from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.deletion import CASCADE
from GeneralModel.models import Firm, FirmAuthorizedPerson
from ProductSystem.models import Inventory, ProductIdentification, ProductOutlet
from multiselectfield import MultiSelectField

RMA_CHOICES = [
    ('hasarli_govde','Hasarli Govde'),
    ('hasarli_psu','Hasarli PSU'),
    ('hasarli_io_port','Hasarli I/O | Port'),
    ('hasarli_ekran_lcd','Hasarli Ekran | LCD'),
    ('hasarli_tus','Hasarli Tus'),
    ('diger','Diger'),
]

class DemoDeliveryForm(models.Model):
    reference_regex = RegexValidator(regex=r'^MM[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$', message="Girmis oldugunuz referans numarasi uygun formatta degildir! (Ornek format: MMTYFN-010121-001)")

    demo_id = models.BigAutoField(primary_key=True, verbose_name='Belge Id')
    reference_number = models.CharField('Referans Numarasi', help_text="Referans numarasini 'MM(ADINIZ)-(6 haneli tarih: GGAAYY)-(BELGE NO)' seklinde giriniz.", max_length=20, blank=False, null=False, validators=[reference_regex,])
    log_date = models.DateTimeField('Tarih', default=datetime.now, blank=False)
    delivery_address = models.TextField('Teslim Adresi', blank=False, null=False)
    client_company = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Musteri')
    client_person = models.ForeignKey(FirmAuthorizedPerson, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ilgili')
    product_id = models.ManyToManyField(ProductIdentification, blank=False, null=False, verbose_name='Urun Bilgisi')

    def __str__(self):
        return str(self.reference_number)

    class Meta:
        verbose_name = 'Demo Teslim Formu'
        verbose_name_plural = 'Demo Teslim Belgeleri'

class DemoProduct(models.Model):
    form_id = models.ForeignKey(DemoDeliveryForm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Form Id')
    product_name = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ürün Adi')
    product_specifications = models.ManyToManyField(ProductIdentification, blank=False, null=False, verbose_name="Bilgiler")
    demo_duration = models.CharField('Demo Süresi', max_length=1000, blank=False, null=False)
    quantity = models.CharField('Adet', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name = 'Demo Ürünü'
        verbose_name_plural = 'Demo Ürünleri'

class DeviceDeliveryForm(models.Model):
    reference_regex = RegexValidator(regex=r'^MM[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$', message="Girmis oldugunuz referans numarasi uygun formatta degildir! (Ornek format: MMTYFN-010121-001)")

    device_delivery_id = models.BigAutoField(primary_key=True, verbose_name='Belge Id')
    reference_number = models.CharField('Referans Numarasi', help_text="Referans numarasini 'MM(ADINIZ)-(6 haneli tarih: GGAAYY)-(BELGE NO)' seklinde giriniz.", max_length=20, blank=False, null=False, validators=[reference_regex,])
    log_date = models.DateTimeField('Tarih', default=datetime.now, blank=False)
    delivery_address = models.TextField('Teslim Adresi', blank=False, null=False)
    client_company = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Musteri')
    client_person = models.ForeignKey(FirmAuthorizedPerson, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ilgili')
    
    def __str__(self):
        return str(self.reference_number)

    class Meta:
        verbose_name = 'Cihaz Teslim Formu'
        verbose_name_plural = 'Cihaz Teslim Belgeleri'

class DeviceDeliveryProduct(models.Model):
    form_id = models.ForeignKey(DeviceDeliveryForm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Form Id')
    product_name = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ürün Adi')
    product_specifications = models.ManyToManyField(ProductIdentification, blank=False, null=False, verbose_name="Bilgiler")
    demo_duration = models.CharField('Teslim Süresi', max_length=1000, blank=False, null=False)
    quantity = models.CharField('Adet', max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.product_name)

    class Meta:
        verbose_name = 'Cihaz Teslim Ürünü'
        verbose_name_plural = 'Cihaz Teslim Ürünleri'

class RMAForm(models.Model):
    rma_no_regex = RegexValidator(regex=r'^RMA[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$', message="Girmis oldugunuz RMA numarasi uygun formatta degildir! (Ornek format: RMATYFN-010121-001")

    rma_form_id = models.BigAutoField(primary_key=True, verbose_name='Belge Id')
    rma_number = models.CharField('RMA Numarasi', help_text="RMA numarasini 'RMA(ADINIZ)-(6 haneli tarih: GGAAYY)-(BELGE NO)' seklinde giriniz.", max_length=20, blank=False, null=False, validators=[rma_no_regex,])
    log_date = models.DateTimeField('Tarih', default=datetime.now, blank=False)
    client_company = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Musteri')
    client_person = models.ForeignKey(FirmAuthorizedPerson, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ilgili')
    entry = models.ForeignKey(Inventory, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Urun Girisi')
    entry_description = models.TextField('Aciklama', blank=False, null=False)
    entry_analysis = MultiSelectField('Inceleme', choices=RMA_CHOICES)
    other_chechked = models.CharField('Tanim', max_length=500)
    entry_note = models.TextField('Not', blank=True, null=True)
    outlet = models.ForeignKey(ProductOutlet, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Urun Cikisi')
    rma_description = models.TextField('Aciklama', blank=True, null=True)
    
    def __str__(self):
        return str(self.rma_number)

    class Meta:
        verbose_name = 'RMA Formu'
        verbose_name_plural = 'RMA Belgeleri'