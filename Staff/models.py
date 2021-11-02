from django.core.validators import RegexValidator
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.template.defaultfilters import truncatechars  # or truncatewords
from GeneralModel.models import Firm, FirmAuthorizedPerson

PERMIT_CHOICES = [
    ('Yillik Izin','Yıllık İzin'),
    ('Saglik Izni','Sağlık İzni'),
    ('Özel Izin','Özel İzin'),
]

PERMIT_TYPE = [
    ('Ücretli Izin', 'Ücretli İzin'),
    ('Ücretsiz Izin', 'Ücretsiz İzin'),
]

COMMUNICATION_TYPE = [
    ('Genel','Genel'),
    ('Telefon','Telefon'),
    ('E-posta','E-posta'),
    ('Toplanti (Online & Yuzyuze)','Toplantı (Online & Yüzyüze)'),
    ('Demo','Demo'),
    ('Egitim (Yuzyuze)','Eğitim (Yüzyüze)'),
    ('Egitim (Online)','Eğitim (Online)'),
    ('Etkinlik','Etkinlik'),
    ('Yazilim','Yazılım'),
    ('Tamir','Tamir')
]

COMPANY_STATUS = [
    ('Eski','Eski'),
    ('Yeni','Yeni'),
]

BUSINESS_STATUS = [
    ('Takipte','Takipte'),
    ('Tamamlanmis','Tamamlanmış'),
    ('Takipsiz','Takipsiz')
]

APPROVAL_STATUS = [
    ('Beklemede','Beklemede'),
    ('Onaylandi','Onaylandı'),
    ('Reddedildi','Reddedildi'),
]

JOB_STATUS = [
    ('Eski', 'Eski'),
    ('Yeni', 'Yeni'),
]
        
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.template.defaultfilters import truncatechars  # or truncatewords

PERMIT_CHOICES = [
    ('Yillik Izin','Yıllık İzin'),
    ('Saglik Izni','Sağlık İzni'),
    ('Özel Izin','Özel İzin'),
]

PERMIT_TYPE = [
    ('Ücretli Izin', 'Ücretli İzin'),
    ('Ücretsiz Izin', 'Ücretsiz İzin'),
]

APPROVAL_STATUS = [
    ('Beklemede','Beklemede'),
    ('Onaylandi','Onaylandı'),
    ('Reddedildi','Reddedildi'),
]

WORK_PROGRESS = [
    ('Takipte','Takipte'),
    ('Tamamlandi','Tamamlandı'),
    ('Takipsiz','Takipsiz')
]

JOB_STATUS = [
    ('Eski', 'Eski'),
    ('Yeni', 'Yeni'),
]

class Report(models.Model):
    report_id = models.BigAutoField(primary_key=True, verbose_name="Rapor Kodu")
    user = models.CharField("Personel Bilgisi", max_length=50, default=User)
    report_date = models.DateTimeField("Rapor Tarihi", default=datetime.now, blank=True, null=True)
    
    def __str__(self):
        return str(self.report_id)
    
    class Meta:
        verbose_name = ("Günlük Rapor")
        verbose_name_plural = ("Günlük Raporlar")

class JobType(models.Model):
    job_id = models.BigAutoField(primary_key=True)
    name = models.CharField("İş Türü", max_length=100, blank=True, null=True)
    #content_id = models.ForeignKey(ReportContent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
    class Meta:
        verbose_name = "İş Türü"
        verbose_name_plural = "İş Türleri"

class AuthorizedPerson (models.Model):
    person_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField("Ad", max_length=50, blank=False, null=False)
    last_name = models.CharField("Soyad", max_length=50, blank=False, null=False)
    job_title = models.CharField("Ünvan", max_length=50, blank=False, null=False)
    phone = models.CharField("Telefon", max_length=15, blank=True, null=True)
    e_mail = models.CharField("E-posta", max_length=100, blank=True, null=True)
    #content_id = models.ForeignKey(ReportContent, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name) + " (" + str(self.job_title) + ")"
    class Meta:
        verbose_name = "Momento Medya İlgili"
        verbose_name_plural = "Momento Medya İlgililer"
        unique_together = ('first_name','last_name')

class ReportContent(models.Model):
    content_id = models.BigAutoField(primary_key=True)
    title = models.CharField("Başlık", max_length = 150, blank=False, null=False)
    job_type = models.ForeignKey(JobType, related_name="job_types", on_delete=models.CASCADE, blank=False, null=False, verbose_name="İş Türü")
    job_status = models.CharField("İş Statüsü", max_length=50, blank=False, null=False, choices=JOB_STATUS)
    #company_info = models.ForeignKey(Company, related_name="companies", on_delete=models.CASCADE, blank=False, null=False)
    work_progress = models.CharField("İş durumu", max_length=100, blank=False, null=False, choices=WORK_PROGRESS)
    related_person = models.ManyToManyField(AuthorizedPerson, related_name="authorized_people", blank=True, null=True, verbose_name="Momento Medya İlgili")
    company = models.ManyToManyField(Firm, related_name="companies", blank=True, null=True, verbose_name="Firma")
    company_authorized = models.ManyToManyField(FirmAuthorizedPerson, related_name="company_people", blank=True, null=True, verbose_name="Firma Yetkilisi")
    description = models.TextField("Açıklama", blank=False, null=False)
    report_document = models.FileField("Ek Belge", upload_to="report_docs/", null=True, blank=True)
    report_id = models.ForeignKey(Report, related_name="reports", on_delete=models.CASCADE,blank=False,null=False)

    def __str__(self):
        return str(self.content_id)

    class Meta:
        verbose_name = "Rapor İçeriği"
        verbose_name_plural = ""


# class TopLevel(models.Model):
#     name = models.CharField(max_length=200)
# class LevelOne(models.Model):
#     name = models.CharField(max_length=200) 
#     level = models.ForeignKey(TopLevel, on_delete=models.CASCADE)
# class LevelTwo(models.Model):
#     name = models.CharField(max_length=200) 
#     level = models.ForeignKey(LevelOne, on_delete=models.CASCADE)
# class LevelThree(models.Model):
#     name = models.CharField(max_length=200) 
#     level = models.ForeignKey(LevelTwo, on_delete=models.CASCADE)

class Employee(models.Model):
    employee_id = models.BigAutoField(primary_key=True, verbose_name="Personel Kodu")
    employee_name = models.CharField("İsim", max_length=50, blank=False, null=False)
    employee_surname = models.CharField("Soy İsim", max_length=50)
    employee_phone = models.CharField("Telefon", max_length=20, blank=False, null=False)
    employee_email = models.EmailField("E-Posta")

    def __str__(self):
        return str(self.employee_name) + " " + str(self.employee_surname) + "-" + str(self.employee_id)

    class Meta:
        verbose_name = ("Personel Kaydı")
        verbose_name_plural = ("Personel Kayıtları")

class AdvanceRequest(models.Model):
    advance_id = models.BigAutoField(primary_key=True, verbose_name="Avans İstek Kodu")
    advance_amount = models.DecimalField("Avans Miktarı", max_digits=11, decimal_places=2,blank=False, null=False)
    request_date = models.DateTimeField("İstek Tarihi", help_text="Avansın çekilmek istenildiği tarih", default=datetime.now, blank=False)
    advance_reason = models.TextField("Neden", blank=True, null=True)
    approval_status = models.CharField("Onay Durumu", max_length=100, choices=APPROVAL_STATUS, default=APPROVAL_STATUS[0][0])
    user = models.CharField("Personel Bilgisi", max_length=50, default=User,)
    
    @property
    def short_description(self):
        return truncatechars(self.advance_reason, 50)
    def __str__(self):
        return str(self.advance_id)

    class Meta:
        verbose_name = ("Avans Talebi")
        verbose_name_plural = ("Avans Talepleri")

class PermitRequest(models.Model):
    permit_id = models.BigAutoField(primary_key=True, verbose_name="İzin İstek Kodu")
    date_start = models.DateTimeField("Başlangıç", default=datetime.now, blank=False)
    date_end = models.DateTimeField ("Bitiş", default=datetime.now, blank=False)
    permit_choice = models.CharField("İzin Kategorisi", max_length=150, blank=False, null=False, choices=PERMIT_CHOICES)
    permit_type = models.CharField("İzin Türü", max_length=100, blank=False, null=False, choices=PERMIT_TYPE)
    permit_reason = models.TextField("Açıklama", blank=True, null=True)
    approval_status = models.CharField("Onay Durumu", max_length=100, choices=APPROVAL_STATUS, default=APPROVAL_STATUS[0][0])
    user = models.CharField("Personel Bilgisi", max_length=50, default=User)
    permit_document = models.FileField("Ek Belge", upload_to="permit_docs/", null=True, blank=True)
    def __str__(self):
        return str(self.permit_id)
    
    class Meta:
        verbose_name = ("İzin Talebi")
        verbose_name_plural = ("İzin Talepleri")