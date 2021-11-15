from datetime import datetime
from django.core.validators import RegexValidator
from django.db import models
from GeneralModel.models import Firm, FirmAuthorizedPerson
from ProductSystem.models import ProductIdentification

# class RMAForm(models.Model):
#     rma_id = models.BigAutoField(primary_key=True, verbose_name='RMA Id')
#     rma_number = models.CharField('RMA Numarasi', max_length=20, blank=False, null=False)


class DemoDeliveryForm(models.Model):
    reference_regex = RegexValidator(regex=r'^MM[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$', message="Girmis oldugunuz referans numarasi uygun formatta degildir! (Ornek format: MMTYFN-010121-001)")

    demo_id = models.BigAutoField(primary_key=True, verbose_name='Belge Id')
    reference_number = models.CharField('Referans Numarasi', help_text="Referans numarasini 'MM(ADINIZ)-(6 haneli tarih: GGAAYY)-(BELGE NO)' seklinde giriniz.", max_length=20, blank=False, null=False, validators=[reference_regex,])
    log_date = models.DateTimeField('Tarih', default=datetime.now, blank=False)
    delivery_address = models.TextField('Teslim Adresi', blank=False, null=False)
    demo_duration = models.CharField('Demo Süresi', max_length=1000, blank=False, null=False)
    client_company = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Musteri')
    client_person = models.ForeignKey(FirmAuthorizedPerson, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ilgili')
    product_id = models.ManyToManyField(ProductIdentification, blank=False, null=False, verbose_name='Urun Bilgisi')

    def __str__(self):
        return str(self.reference_number)

    class Meta:
        verbose_name = 'Demo Teslim Formu'
        verbose_name_plural = 'Demo Teslim Belgeleri'

class DeviceDeliveryForm(models.Model):
    reference_regex = RegexValidator(regex=r'^MM[A-Z]{2,8}-[0-9]{6}-[0-9]{3}$', message="Girmis oldugunuz referans numarasi uygun formatta degildir! (Ornek format: MMTYFN-010121-001)")

    device_delivery_id = models.BigAutoField(primary_key=True, verbose_name='Belge Id')
    reference_number = models.CharField('Referans Numarasi', help_text="Referans numarasini 'MM(ADINIZ)-(6 haneli tarih: GGAAYY)-(BELGE NO)' seklinde giriniz.", max_length=20, blank=False, null=False, validators=[reference_regex,])
    log_date = models.DateTimeField('Tarih', default=datetime.now, blank=False)
    delivery_address = models.TextField('Teslim Adresi', blank=False, null=False)
    return_date = models.DateTimeField('Dönüs Tarihi', blank=False, null=False)
    client_company = models.ForeignKey(Firm, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Musteri')
    client_person = models.ForeignKey(FirmAuthorizedPerson, on_delete=models.CASCADE, blank=False, null=False, verbose_name='Ilgili')
    product_id = models.ManyToManyField(ProductIdentification, blank=False, null=False, verbose_name='Urun Bilgisi')

    def __str__(self):
        return str(self.reference_number)

    class Meta:
        verbose_name = 'Cihaz Teslim Formu'
        verbose_name_plural = 'Cihaz Teslim Belgeleri'