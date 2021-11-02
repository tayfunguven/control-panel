from django.db import models
from django.core.validators import RegexValidator

class Firm(models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!")

    firm_id = models.BigAutoField(primary_key = True, verbose_name="Firma Kodu")
    company_name = models.CharField("Ad", max_length=300, blank=False, null=False)
    business_field = models.CharField("İş alanı", max_length=150, blank=False, null=False)
    e_mail = models.EmailField("E-Posta", blank=True, null=True)
    phone = models.CharField("Telefon", max_length=15, blank=True, null=True, validators=[phone_regex])
    address = models.TextField("Adres", blank=True, null=True) 
    has_invoice = models.BooleanField("Fatura bilgisi", blank=True, default=False)
    tax_administration = models.TextField("Vergi Dairesi", blank=True, null=True)
    tax_number = models.CharField("Vergi Numarasi", blank=True, null=True, max_length=200)
    mersis_number = models.CharField("Mersis No", blank=True, null=True, max_length=200)
    company_title = models.CharField("Firma Unvani", blank=True, null=True, max_length=300)
    official_address = models.TextField("Resmi Adres", blank=True, null=True)

    def __str__(self):
        if self.company_title is not None:
            return str(self.company_title)
        return str(self.company_name)

    class Meta:
        verbose_name = 'Sirket'
        verbose_name_plural = 'Sirketler'

class FirmAuthorizedPerson (models.Model):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Telefon formatı '+9XXXXXXXXXXX' şeklinde olmalıdır!")

    person_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField("Ad", max_length=100, blank=False, null=False)
    last_name = models.CharField("Soyad", max_length=100, blank=False, null=False)
    authorized_title = models.CharField("Unvan", max_length=50, blank=False, null=False)
    company = models.ForeignKey(Firm, related_name="firm_authorizeds", on_delete=models.CASCADE, blank=False, null=False, verbose_name="Firma")
    phone = models.CharField("Telefon", max_length=15, blank=False, null=True, validators=[phone_regex])
    e_mail = models.CharField("E-posta", max_length=100, blank=False, null=True)
 
    #company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) + " (" + str(self.company) + ")"
    class Meta:
        verbose_name = "Sirket Yetkilisi"
        verbose_name_plural = "Sirket Yetkilileri"
        unique_together = ('first_name','last_name')
        
class DeliveryCompany(models.Model):
    delivery_company_id = models.BigAutoField(primary_key=True, verbose_name="Firma Kodu")
    cargo_name = models.CharField("Teslimat Firması", max_length=150, blank=False, null=False)
    cargo_branch = models.CharField("Teslimat Subesi", max_length=150, blank=True, null=True)
    
    def __str__(self):
        return str(self.cargo_name) + " (" +  str(self.cargo_branch) + ")"

    class Meta:
        verbose_name = "Teslimat Firması"
        verbose_name_plural = "Teslimat Firmaları"