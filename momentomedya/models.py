from django.core.validators import RegexValidator
from django.db import models
from django.db.models import fields
from multiselectfield.db.fields import MultiSelectField

RMA_CHOICES = [
    ('hasarli_govde','Hasarli Govde'),
    ('hasarli_psu','Hasarli PSU'),
    ('hasarli_io_port','Hasarli I/O | Port'),
    ('hasarli_ekran_lcd','Hasarli Ekran | LCD'),
    ('hasarli_tus','Hasarli Tus'),
    ('diger','Diger'),
]

class RMAApply(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!")
    
    apply_id = models.BigAutoField(primary_key=True, verbose_name="Basvuru Id")
    customer_first_name = models.CharField("Adınız*", max_length=100, blank=False, null=False)
    customer_last_name = models.CharField("Soyadınız*", max_length=100, blank=False, null=False)
    customer_company = models.CharField("Firma İsmi", max_length=300, blank=True, null=True)
    customer_email = models.EmailField("E-Posta*", blank=False, null=False )
    customer_phone = models.CharField("Telefon Numarası*", max_length=20, blank=False, null=False, validators=[phone_regex,])
    customer_address = models.TextField("Adres", blank=True, null=True )
    product_brand = models.CharField("Marka*", max_length=100, blank=False, null=False)
    product_model = models.CharField("Model*", max_length=500, blank=False, null=False)
    product_serial = models.CharField("Cihaz Seri No*", max_length=200, blank=False, null=False)
    apply_topic = models.CharField("Ariza Bildirisi Konusu*", max_length=500, blank=False, null=False)
    problems = MultiSelectField('Problem', choices=RMA_CHOICES)
    problem_note = models.TextField("Açıklama*", blank=False, null=False)
    #other_chechked = models.TextField('Tanım', blank=True, null=True)
    #pdpb_approval = models.BooleanField('KVKK Onayi')

    def _str_(self):
        return str(self.apply_id) + " " + str(self.apply_topic)

    class Meta:
        verbose_name = 'RMA Basvurusu'
        verbose_name_plural = 'RMA Basvurulari'

class CareerApply(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!")
    
    inputName = models.CharField("İsim", max_length=100, blank=False, null=False)
    inputSurname= models.CharField("Soyadı", max_length=100, blank=False, null=False)
    inputEmail= models.EmailField("E-Posta Adresi", blank=False, null=False)
    inputPhone= models.CharField("Telefon Numarası", max_length=20, blank=False, null=False, validators=[phone_regex,])
    inputMessage= models.TextField("Mesajınız", blank=False, null=False)

    class Meta:
        verbose_name = 'Career Page'
        verbose_name_plural = 'Career Pages'