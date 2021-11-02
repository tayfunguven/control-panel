from ProductSystem.models import Inventory
import datetime
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime as dt
import datetime
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
PROJECT_STATUS = (
    ('takipte','Takipte'),
    ('tamamlandi','Tamamlandı'),
    ('takipsiz','Takipsiz'),
    ('iptal', 'İptal'),
)

APPROVAL_STATUS = [
    ('beklemede','Beklemede'),
    ('onaylandi','Onaylandı'),
    ('reddedildi','Reddedildi'),
    ('bosta', 'Boşta'),
]

class RegisterDeal(models.Model):   
    def validate_initial_date(value):
        if value < dt.date(dt.now()):
            raise ValidationError('Sadece bugün ve ileriye dönük anlaşma tarihi giriniz!')
    def validate_date(value):
        diff = value - dt.date(dt.now())
        print(diff)
        if diff.days>=91:
            raise ValidationError('En fazla 3 ay (90 gün) ileriye tahmini teslimat tarihi verebilirsiniz! Girdiğiniz gün = %s ' %diff.days)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Telefon formatı '+XXXXXXXXXXX' şeklinde olmalıdır!")
    
    is_displayed = models.BooleanField("Herkese açık olarak gösterilsin mi?", default=False)
    deal_id = models.BigAutoField(primary_key=True, verbose_name="Proje ID")
    project_name = models.CharField("Proje Adı", max_length=250, blank=False, null=False, unique=True)
    project_subject = models.CharField("Proje Konusu", max_length=250, blank=False, null=False)
    approval = models.CharField("Onay Durumu", max_length=20, blank=False, null=False, choices=APPROVAL_STATUS, default=APPROVAL_STATUS[0][0])
    project_date = models.DateField("Proje Tarihi", default=dt.date(dt.now()),)
    estimated_date = models.DateField("Tahmini Teslim Tarihi", validators=[validate_date, validate_initial_date])
    project_time = models.IntegerField("Proje Süresi", blank=False, null=False,)
    manager_note = models.TextField("Açıklama (Momento Medya)", blank=False, null=False)
    user = models.CharField("Düzenleyen", max_length=100, default=User)
    project_status = models.CharField("İlerleme Durumu", max_length=150, blank=False, null=False, choices=PROJECT_STATUS, default=PROJECT_STATUS[0][0])
    project_description = models.TextField("Açıklama")
    company = models.CharField("Kurum Adı", max_length=150, blank=False, null=False)
    company_address = models.TextField("Kurum Adresi", blank=False, null=False)
    contact_name = models.CharField("Ad", max_length=150, blank=False, null=False)
    contact_surname = models.CharField("Soyad", max_length=150, blank=False, null=False)
    contact_phone = models.CharField("Telefon", help_text="+ÜLKEKODU5555555555", validators=[phone_regex], max_length=17, blank=False, null=False, default="+")
    contact_email = models.CharField("E-posta", max_length=150, blank=False, null=False)

    def save(self, *args, **kwargs):
        from django.db import transaction
        self.project_time = str((self.estimated_date - self.project_date).days)
        try:
            with transaction.atomic():
                if self.pk is None:
                    a = RegisterLogs(
                        is_displayed = self.is_displayed,
                        project_name = self.project_name + " (İLK KAYIT)",
                        project_subject = self.project_subject,
                        project_date = self.project_date,
                        estimated_date = self.estimated_date,
                        project_time = self.project_time,
                        user = self.user,
                        project_status = self.project_status,
                        project_description = self.project_description,
                        company = self.company,
                        company_address = self.company_address,
                        contact_name = self.contact_name,
                        contact_surname = self.contact_surname,
                        contact_phone = self.contact_phone,
                        contact_email = self.contact_email
                    )
                    a.save()
                else:
                    b = RegisterLogs(
                        is_displayed = self.is_displayed,
                        project_name = self.project_name + " (GÜNCELLEME TARİHİ: " + str(datetime.datetime.now().strftime("%b %d %Y %H:%M:%S")) + ")",
                        project_subject = self.project_subject,
                        project_date = self.project_date,
                        estimated_date = self.estimated_date,
                        project_time = self.project_time,
                        user = self.user,
                        project_status = self.project_status,
                        project_description = self.project_description,
                        company = self.company,
                        company_address = self.company_address,
                        contact_name = self.contact_name,
                        contact_surname = self.contact_surname,
                        contact_phone = self.contact_phone,
                        contact_email = self.contact_email
                    )
                    b.save()
        except Exception as e:
            print(e)
        super(RegisterDeal, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name = "Proje Kaydı"
        verbose_name_plural = "Proje Kayıtlarım"

class RegisterLogs(models.Model):
    is_displayed = models.BooleanField("Herkese açık olarak gösterilsin mi?", editable=True)
    log_id = models.BigAutoField(primary_key=True, verbose_name="Proje ID")
    project_name = models.CharField("Proje Adı", max_length=250, blank=False, null=False)
    project_subject = models.CharField("Proje Konusu", max_length=250, blank=False, null=False)
    approval = models.CharField("Onay Durumu", max_length=20, blank=False, null=False, choices=APPROVAL_STATUS, default=APPROVAL_STATUS[0][0])
    project_date = models.DateField("Proje Tarihi",)
    estimated_date = models.DateField("Tahmini Teslim Tarihi",)
    project_time = models.IntegerField("Proje Süresi", blank=False, null=False,)
    manager_note = models.TextField("Açıklama (Momento Medya)", blank=True, null=True)
    user = models.CharField("Düzenleyen", max_length=100, default=User)
    project_status = models.CharField("İlerleme Durumu", max_length=150, blank=False, null=False, choices=PROJECT_STATUS, default=PROJECT_STATUS[0][0])
    project_description = models.TextField("Açıklama")
    company = models.CharField("Kurum Adı", max_length=150, blank=False, null=False)
    company_address = models.TextField("Kurum Adresi", blank=False, null=False)
    contact_name = models.CharField("Ad", max_length=150, blank=False, null=False)
    contact_surname = models.CharField("Soyad", max_length=150, blank=False, null=False)
    contact_phone = models.CharField("Telefon", max_length=15, blank=False, null=False)
    contact_email = models.CharField("E-posta", max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.project_name)

    class Meta:
        verbose_name = "Proje Güncelleme Listesi"
        verbose_name_plural = "Proje Güncellemeleri Listesi"

class Dealer(models.Model):
    dealer_id = models.BigAutoField(primary_key=True, verbose_name="Bayi ID")
    dealer_name = models.CharField("Bayi", max_length=200, blank=False,null=False)

    def __str__(self):
        return str(self.dealer_name)

    class Meta:
        verbose_name = "Bayi"
        verbose_name_plural = "Bayiler"

class DealerUser(models.Model):
    user_id = models.BigAutoField(primary_key=True, verbose_name="Bayi ID")
    dealer = models.ForeignKey(Dealer, related_name="dealers", on_delete=models.CASCADE, blank=False, null=False, verbose_name="Bayi")
    user = models.CharField("Kullanıcı", max_length=200, blank=False,null=False, default=User)

    def __str__(self):
        return str(self.dealer) + " " + str(self.user)

    class Meta:
        verbose_name = "Bayi Kullanıcısı"
        verbose_name_plural = "Bayi Kullanıcıları"
    

class DealerProjectSummary(RegisterLogs):
    class Meta:
        proxy = True
        verbose_name = 'Proje'
        verbose_name_plural = 'Tüm Bayi Projeleri'

class InventoryForDealer(Inventory):
    class Meta:
        proxy = True
        verbose_name = 'Momento Medya Envanter'
        verbose_name_plural = 'Momento Medya Envanter'