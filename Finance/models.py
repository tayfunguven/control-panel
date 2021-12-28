import string
from django.db import models
from django.utils.crypto import get_random_string
from decimal import Decimal
from forex_python.converter import CurrencyRates, RatesNotAvailableError
from datetime import datetime as dt
from django.db import transaction
from django.contrib.auth import get_user_model
import datetime
import calendar
from django.contrib.auth.models import User as usr
import sys, os

APPROVAL_STATUS = [
    ('Onay Surecinde', 'Onay Sürecinde'),
    ('Onay', 'Onay'),
    ('Ret', 'Ret'),
]

MONEY_UNIT = [
    ('₺ (TRY)','₺ (TRY)'),
    ('€ (EUR)','€ (EUR)'),
    ('$ (USD)','$ (USD)'),
]

PAYMENT_TYPE = [
    ('Nakit','Nakit'),
    ('Kredi Kart', 'Kredi Kartı'),
    ('EFT/Havale','EFT/Havale'),
    ('Çek','Çek'),
    ('Senet','Senet'),
    ('Uluslararası Para Transferi', 'Uluslararası Para Transferi')
]

PAYMENT_STATUS = [
    ('Odenmedi','Ödenmedi'),
    ('Odendi','Ödendi'),
]

def get_curenncy_rates(type, date_of_rate):   
    c = CurrencyRates() 
    try:  
        return Decimal(c.get_rate(str(type), 'TRY', date_of_rate))
    except RatesNotAvailableError as e:
        print(e)
        day = calendar.day_name[date_of_rate.weekday()]
        # print(day)
        if (day == 'Monday'):
            print(date_of_rate-datetime.timedelta(days=3))
            updated_date = date_of_rate - datetime.timedelta(days=3)
            return Decimal(c.get_rate(str(type), 'TRY', updated_date))
        elif (day == 'Sunday'):
            print(date_of_rate-datetime.timedelta(days=2))
            updated_date = date_of_rate - datetime.timedelta(days=2)
            return Decimal(c.get_rate(str(type), 'TRY', updated_date))
        elif (str(e) == 'Currency Rates Source Not Ready'):
            return Decimal(c.get_rate(str(type), 'TRY'))
        else:
            print(date_of_rate-datetime.timedelta(days=1))
            updated_date = date_of_rate - datetime.timedelta(days=1)
            return Decimal(c.get_rate(str(type), 'TRY', updated_date))
    except Exception as e:
        print(e)
        

# Users = get_user_model()
# users = tuple(Users.objects.values_list('username', 'username'))
USER_NAMES = [
    ('admin','admin')
]

class Incentive(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    incentive_id = models.BigAutoField(primary_key=True, verbose_name="Teşvik ID")
    incentive_code = models.CharField("Teşvik Kodu", blank=False, null=False, max_length=8, default=generate_unique_code)
    user = models.CharField("Personel", max_length=200, blank=False, null=False, choices=USER_NAMES)
    incentive_name = models.CharField("Konu", max_length=350, blank=False, null=False)
    incentive_amount = models.IntegerField("Teşvik Tutarı", blank=False, null=False)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))
    
    def __str__(self):
        return str(self.incentive_name)

    class Meta:
        verbose_name = "Teşvik"
        verbose_name_plural = "Teşvikler"

    def save(self, *args, **kwargs):
        from django.db import transaction
        try:
            with transaction.atomic():
                if self.pk is None:
                    a = PersonalIncome(
                        income_code = self.incentive_code,
                        income_name = "TEŞVİK",
                        unit_id = UnitName.objects.first(),
                        currency_price = self.incentive_amount,
                        amount = 1,
                        vat_rate = 0,
                        user = self.user
                    )
                    a.save()
                    b = CompanyExpense(
                        expense_code = self.incentive_code,
                        expense_name = "TEŞVİK",
                        unit_id = UnitName.objects.first(),
                        currency_price = self.incentive_amount,
                        amount = 1,
                        vat_rate = 0,
                        expense_to = self.user
                    )
                    b.save()
                else:
                    PersonalIncome.objects.filter(income_code=self.incentive_code).update(
                        currency_price = self.incentive_amount,
                        vat_rate = 0,
                        grand_total = self.incentive_amount,
                        price = self.incentive_amount,
                        subtotal = self.incentive_amount
                    )
                    CompanyExpense.objects.filter(expense_code=self.incentive_code).update(
                        currency_price = self.incentive_amount,
                        vat_rate = 0,
                        grand_total = self.incentive_amount,
                        price = self.incentive_amount,
                        subtotal = self.incentive_amount
                    )
        except Exception as e:
            print("EXCEPTION ----> : " + str(e))
        super(Incentive, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        CompanyExpense.objects.filter(expense_code = self.incentive_code).delete()
        PersonalIncome.objects.filter(income_code = self.incentive_code).delete()
        Incentive.objects.filter(incentive_code = self.incentive_code).delete()
        super(Incentive, self).delete(*args, **kwargs)

class AdvancePayment(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    payment_id = models.BigAutoField(primary_key=True, verbose_name="Ödeme ID")
    payment_code = models.CharField("Avans Kodu", blank=False, null=False, max_length=8, default=generate_unique_code)
    user = models.CharField("Personel", max_length=200, blank=False, null=False, choices=USER_NAMES)
    description = models.TextField("Aciklama", blank=True, null=True)
    payment_amount = models.DecimalField("Avans Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))

    def __str__(self):
        return str(self.payment_id) + " " + str(self.user)

    class Meta:
        verbose_name = "Avans Ödemesi"
        verbose_name_plural = "Avans Ödemeleri"

    def save(self, *args, **kwargs):
        try:
            with transaction.atomic():
                if self.pk is None:
                    a = PersonalIncome(
                        income_code = self.payment_code,
                        income_name = "AVANS",
                        currency_price = self.payment_amount,
                        unit_id = UnitName.objects.first(),
                        amount = 1,
                        vat_rate = 0,
                        user = self.user
                    )
                    a.save()
                    b = CompanyExpense(
                        expense_code = self.payment_code,
                        expense_name = "AVANS",
                        unit_id = UnitName.objects.first(),
                        currency_price = self.payment_amount,
                        amount = 1,
                        vat_rate = 0,
                        expense_to = self.user
                    )
                    b.save()
                else:
                    PersonalIncome.objects.filter(income_code=self.payment_code).update(
                        currency_price = self.payment_amount,
                        vat_rate = 0,
                        grand_total = self.payment_amount,
                        price = self.payment_amount,
                        subtotal = self.payment_amount
                    )
                    CompanyExpense.objects.filter(expense_code=self.payment_code).update(
                        currency_price = self.payment_amount,
                        vat_rate = 0,
                        grand_total = self.payment_amount,
                        price = self.payment_amount,
                        subtotal = self.payment_amount
                    )
        except Exception as e:
            print("EXCEPTION ----> : " + str(e))
        super(AdvancePayment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        CompanyExpense.objects.filter(expense_code = self.payment_code).delete()
        PersonalIncome.objects.filter(income_code = self.payment_code).delete()
        AdvancePayment.objects.filter(payment_code = self.payment_code).delete()
        super(AdvancePayment, self).delete(*args, **kwargs)

class Punishment(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    punishment_id = models.BigAutoField(primary_key=True, verbose_name="Ceza ID")
    punishment_code = models.CharField("Ceza Kodu", blank=False, null=False, max_length=8, default=generate_unique_code)
    user = models.CharField("Personel", max_length=200, blank=False, null=False, choices=USER_NAMES)
    punishment_topic = models.CharField("Başlık", max_length=200, blank=False, null=False)
    punishment_amount = models.DecimalField("Ceza Tutarı", decimal_places=2, max_digits=25, blank=False, null=False)
    punishment_explanation = models.TextField("Açıklama", blank=False, null=False)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))

    def __str__(self):
        return str(self.punishment_topic)

    class Meta:
        verbose_name = "Ceza"
        verbose_name_plural = "Cezalar"
    
    def save(self, *args, **kwargs):
        from django.db import transaction
        try:
            with transaction.atomic():
                if self.pk is None:
                    a = PersonalExpense(
                        expense_code = self.punishment_code,
                        expense_name = "CEZA",
                        currency_price = self.punishment_amount,
                        unit_id = UnitName.objects.first(),
                        amount = 1,
                        vat_rate = 0,
                        user = self.user
                    )
                    a.save()
                else:
                    PersonalExpense.objects.filter(expense_code=self.punishment_code).update(
                        currency_price = self.punishment_amount,
                        vat_rate = 0,
                        grand_total = self.punishment_amount,
                        price = self.punishment_amount,
                        subtotal = self.punishment_amount
                    )
        except Exception as e:
            print("EXCEPTION ----> : " + str(e))
        super(Punishment, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        PersonalExpense.objects.filter(expense_code = self.punishment_code).delete()
        Punishment.objects.filter(punishment_code = self.punishment_code).delete()
        super(Punishment, self).delete(*args, **kwargs)

class SalaryInfo(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    salary_info_id = models.BigAutoField(primary_key=True, verbose_name="Salary Info ID")
    salary_info_code = models.CharField("Maaş Kodu", max_length=8, blank=False, null=False, default=generate_unique_code)
    user = models.CharField("Personel", max_length=200, blank=False, null=False, choices=USER_NAMES)
    salary = models.DecimalField("Maaş", blank=False, null=False, max_digits=25, decimal_places=2)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))

    def __str__(self):
        return str(self.salary_info_id)

    class Meta:
        verbose_name = "Maaş"
        verbose_name_plural = "Maaşlar"

    def save(self, *args, **kwargs):
        from django.db import transaction
        try:
            with transaction.atomic():
                if self.pk is None:
                    a = PersonalIncome(
                        income_code = self.salary_info_code,
                        income_name = "MAAŞ",
                        currency_price = self.salary,
                        unit_id = UnitName.objects.first(),
                        amount = 1,
                        vat_rate = 0,
                        user = self.user
                    )
                    a.save()
                    b = CompanyExpense(
                        expense_code = self.salary_info_code,
                        expense_name = "MAAŞ",
                        unit_id = UnitName.objects.first(),
                        currency_price = self.salary,
                        amount = 1,
                        vat_rate = 0,
                        expense_to = self.user
                    )
                    b.save()
                else:
                    PersonalIncome.objects.filter(income_code=self.salary_info_code).update(
                        currency_price = self.salary,
                        vat_rate = 0,
                        grand_total = self.salary,
                        price = self.salary,
                        subtotal = self.salary
                    )
                    CompanyExpense.objects.filter(expense_code=self.salary_info_code).update(
                        currency_price = self.salary,
                        vat_rate = 0,
                        grand_total = self.salary,
                        price = self.salary,
                        subtotal = self.salary
                    )
        except Exception as e:
            print("EXCEPTION ----> : " + str(e))
        super(SalaryInfo, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        CompanyExpense.objects.filter(expense_code = self.salary_info_code).delete()
        PersonalIncome.objects.filter(income_code = self.salary_info_code).delete()
        SalaryInfo.objects.filter(salary_info_code = self.salary_info_code).delete()
        super(SalaryInfo, self).delete(*args, **kwargs)

class Comission(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    comission_id = models.BigAutoField(primary_key=True, verbose_name="Prim ID")
    comission_code = models.CharField("Prim kodu", max_length=8, default=generate_unique_code)
    type_id = models.CharField("Komisyon Türü", max_length=100, blank=True, null=True)
    sales_price = models.DecimalField("Satış Fiyatı", max_digits=25, decimal_places=2, blank=False, null=False)
    comission_rate = models.IntegerField("Komisyon Oranı (%)", default=0, blank=False, null=False)
    total = models.DecimalField("Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))
    user = models.CharField("Personel", max_length=200, blank=False, null=False, choices=USER_NAMES)
    
    def __str__(self):
        return str(self.comission_id)

    class Meta:
        verbose_name = "Komisyon/Prim"
        verbose_name_plural = "Komisyonlar/Primler"

    def save(self,*args, **kwargs):      
        from django.db import transaction
        try:
            with transaction.atomic():
                if self.pk is None:
                    self.total = self.sales_price * (Decimal(self.comission_rate)/100)
                    a = PersonalIncome(
                        income_name = "KOMİSYON/PRİM",
                        income_code = self.comission_code,
                        currency_price = self.total,
                        unit_id = UnitName.objects.first(),
                        amount = 1,
                        vat_rate = 0,
                        user = self.user
                    )   
                    a.save()   
                    b = CompanyExpense(
                        expense_code = self.comission_code,
                        expense_name = "KOMİSYON/PRİM",
                        unit_id = UnitName.objects.first(),
                        currency_price = self.total,
                        amount = 1,
                        vat_rate = 0,
                        expense_to = self.user
                    )
                    b.save() 
                else:
                    self.total = 0
                    self.total = self.sales_price * (Decimal(self.comission_rate)/100) 
                    PersonalIncome.objects.filter(income_code=self.comission_code).update(
                        currency_price = self.total,
                        vat_rate = 0,
                        grand_total = self.total,
                        price = self.total,
                        subtotal = self.total
                    )      
                    CompanyExpense.objects.filter(expense_code=self.comission_code).update(
                        currency_price = self.total,
                        vat_rate = 0,
                        grand_total = self.total,
                        price = self.total,
                        subtotal = self.total
                    )             
        except Exception as e:
            print("EXCEPTION ----> : " + str(e))
        super(Comission, self).save(*args, **kwargs)      

    def delete(self, *args, **kwargs):
        CompanyExpense.objects.filter(expense_code = self.comission_code).delete()
        PersonalIncome.objects.filter(income_code = self.comission_code).delete()
        Comission.objects.filter(comission_code = self.comission_code).delete()
        super(Comission, self).delete(*args, **kwargs)

class UnitName(models.Model):
    unit_id = models.BigAutoField(primary_key=True, verbose_name="Birim ID")
    unit_name = models.CharField("Birim Adı", max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.unit_name)

    class Meta:
        verbose_name = "Birim"
        verbose_name_plural = "Birimler"

class PersonalExpenseTable(models.Model):
    table_id = models.BigAutoField(primary_key=True, verbose_name="Tablo Kodu")
    
    def __str__(self):
        return str(self.table_id)
    
    class Meta:
        verbose_name = "Bireysel Gider Girişi"
        verbose_name_plural = "Bireysel Giderler"

class PersonalExpense(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    expense_id = models.BigAutoField(primary_key=True, verbose_name="Gider ID")
    expense_code = models.CharField("Gider Kodu", max_length=8, default=generate_unique_code)
    expense_name = models.CharField("Gider Adı", max_length=100, blank=False, null=False)
    amount = models.DecimalField("Miktar", blank=False, null=False, max_digits=20, decimal_places=2)
    unit_id = models.ForeignKey(UnitName, related_name="expense_units", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Birim")
    currency_price = models.DecimalField("Döviz Fiyatı", blank=False, null=False, max_digits=20, decimal_places=2, default=0.00)
    currency_type = models.CharField("Döviz Cinsi", max_length=15, choices=MONEY_UNIT, default=MONEY_UNIT[0][0])
    price = models.DecimalField("Fiyat", max_digits=25, decimal_places=2, blank=False, null=False)
    subtotal = models.DecimalField("Ara Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    vat_rate = models.IntegerField("KDV Oranı (%)", default=0, blank=False, null=False)
    vat_amount = models.DecimalField("KDV Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField("Genel Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    table_id = models.ForeignKey(PersonalExpenseTable, on_delete=models.CASCADE, verbose_name="Giriş Bilgisi", editable=False, null=True, blank=True)
    user = models.CharField("Kullanıcı", max_length=200, blank=False, null=False, choices=USER_NAMES)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))

    def save(self):
        if self.pk is None:
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = Decimal(CurrencyRates().get_rate('TRY','TRY'))
            elif currency_type == MONEY_UNIT[1][0]:
                default = Decimal(CurrencyRates().get_rate('EUR','TRY'))
            elif currency_type == MONEY_UNIT[2][0]:
                default = Decimal(CurrencyRates().get_rate('USD','TRY'))
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        else:
            self.price = 0
            self.subtotal = 0
            self.vat_amount = 0
            self.grand_total = 0
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = get_curenncy_rates('TRY', self.log_date)
            elif currency_type == MONEY_UNIT[1][0]:
                default = get_curenncy_rates('EUR', self.log_date)
            elif currency_type == MONEY_UNIT[2][0]:
                default = get_curenncy_rates('USD', self.log_date)
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        return super(PersonalExpense, self).save()

    def delete(self, *args, **kwargs):
        Punishment.objects.filter(punishment_code = self.expense_code).delete()
        PersonalExpenseForUserEntry.objects.filter(expense_code = self.expense_code).delete()
        PersonalExpense.objects.filter(expense_code = self.expense_code).delete()
        super(PersonalExpense, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.expense_code)

    class Meta:
        verbose_name = "Bireysel Gider"
        verbose_name_plural = "Bireysel Gider Listesi"

class PersonalIncomeTable(models.Model):
    table_id = models.BigAutoField(primary_key=True, verbose_name="Tablo Kodu")

    def __str__(self):
        return str(self.table_id)

    class Meta:
        verbose_name = "Bireysel Gelir Girişi"
        verbose_name_plural = "Bireysel Gelirler"

class PersonalIncome(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    income_id = models.BigAutoField(primary_key=True, verbose_name="Gelir ID")
    income_code = models.CharField("Gelir Kodu", max_length=8, default=generate_unique_code)
    income_name = models.CharField("Gelir Adı", max_length=100, blank=False, null=False)
    amount = models.DecimalField("Miktar", blank=False, null=False, max_digits=20, decimal_places=2)
    unit_id = models.ForeignKey(UnitName, related_name="income_units", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Birim")
    currency_price = models.DecimalField("Döviz Fiyatı", blank=False, null=False, max_digits=20, decimal_places=2, default=0.00)
    currency_type = models.CharField("Döviz Cinsi", max_length=15, choices=MONEY_UNIT, default=MONEY_UNIT[0][0])
    price = models.DecimalField("Fiyat", max_digits=25, decimal_places=2, blank=False, null=False)
    subtotal = models.DecimalField("Ara Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    vat_rate = models.IntegerField("KDV Oranı (%)", default=0, blank=False, null=False)
    vat_amount = models.DecimalField("KDV Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField("Genel Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    table_id = models.ForeignKey(PersonalIncomeTable, on_delete=models.CASCADE, verbose_name="Giriş Bilgisi", editable=False, blank=True, null=True)
    user = models.CharField("Kullanıcı", max_length=200, blank=False, null=False, choices=USER_NAMES)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))

    def save(self):
        if self.pk is None:
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = Decimal(CurrencyRates().get_rate('TRY','TRY'))
            elif currency_type == MONEY_UNIT[1][0]:
                default = Decimal(CurrencyRates().get_rate('EUR','TRY'))
            elif currency_type == MONEY_UNIT[2][0]:
                default = Decimal(CurrencyRates().get_rate('USD','TRY'))
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        else:
            self.price = 0
            self.subtotal = 0
            self.vat_amount = 0
            self.grand_total = 0
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = get_curenncy_rates('TRY', self.log_date)
            elif currency_type == MONEY_UNIT[1][0]:
                default = get_curenncy_rates('EUR', self.log_date)
            elif currency_type == MONEY_UNIT[2][0]:
                default = get_curenncy_rates('USD', self.log_date)
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        return super(PersonalIncome, self).save()

    def delete(self, *args, **kwargs):
        Incentive.objects.filter(incentive_code = self.income_code).delete()
        AdvancePayment.objects.filter(payment_code = self.income_code).delete()
        CompanyExpense.objects.filter(expense_code = self.income_code).delete()
        SalaryInfo.objects.filter(salary_info_code = self.income_code).delete()
        Comission.objects.filter(comission_code = self.income_code).delete()
        PersonalExpenseForUserEntry.objects.filter(expense_code = self.income_code).update(
            approval_status = APPROVAL_STATUS[0][0],
            payment_status = PAYMENT_STATUS[0][0]
        )
        PersonalIncome.objects.filter(income_code=self.income_code).delete()
        super(PersonalIncome, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.income_code)

    class Meta:
        verbose_name = "Bireysel Gelir"
        verbose_name_plural = "Bireysel Gelir Listesi"
    
class CompanyIncomeTable(models.Model):
    table_id = models.BigAutoField(primary_key=True, verbose_name="Tablo Kodu")
    
    def __str__(self):
        return str(self.table_id)
    
    class Meta:
        verbose_name = "Şirket Gelir Girişi"
        verbose_name_plural = "Şirket Gelirleri"

class CompanyIncome(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    income_id = models.BigAutoField(primary_key=True, verbose_name="Gelir ID")
    income_code = models.CharField("Gelir Kodu", max_length=8, default=generate_unique_code)
    income_name = models.CharField("Gelir Adı", max_length=100, blank=False, null=False)
    amount = models.DecimalField("Miktar", blank=False, null=False, max_digits=20, decimal_places=2)
    unit_id = models.ForeignKey(UnitName, related_name="company_income_units", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Birim")
    currency_price = models.DecimalField("Döviz Fiyatı", blank=False, null=False, max_digits=20, decimal_places=2, default=0.00)
    currency_type = models.CharField("Döviz Cinsi", max_length=15, choices=MONEY_UNIT, default=MONEY_UNIT[0][0])
    price = models.DecimalField("Fiyat", max_digits=25, decimal_places=2, blank=False, null=False, default=0)
    subtotal = models.DecimalField("Ara Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    vat_rate = models.IntegerField("KDV Oranı (%)", default=0, blank=False, null=False)
    vat_amount = models.DecimalField("KDV Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField("Genel Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    payment_type = models.CharField("Gelir Türü", max_length=200, blank=False, null=False, default=PAYMENT_TYPE[0][0], choices=PAYMENT_TYPE)
    table_id = models.ForeignKey(CompanyIncomeTable, on_delete=models.CASCADE, verbose_name="Giriş Bilgisi", editable=False, blank=True, null=True)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))
    income_to = models.CharField("Kime/Nereye", max_length=200, blank=False, null=False)

    def save(self):
        if self.pk is None:
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = Decimal(CurrencyRates().get_rate('TRY','TRY'))
            elif currency_type == MONEY_UNIT[1][0]:
                default = Decimal(CurrencyRates().get_rate('EUR','TRY'))
            elif currency_type == MONEY_UNIT[2][0]:
                default = Decimal(CurrencyRates().get_rate('USD','TRY'))
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        else:
            self.price = 0
            self.subtotal = 0
            self.vat_amount = 0
            self.grand_total = 0
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = get_curenncy_rates('TRY', self.log_date)
            elif currency_type == MONEY_UNIT[1][0]:
                default = get_curenncy_rates('EUR', self.log_date)
            elif currency_type == MONEY_UNIT[2][0]:
                default = get_curenncy_rates('USD', self.log_date)
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        return super(CompanyIncome, self).save()

    def __str__(self):
        return str(self.income_code) + " " + str(self.income_name)

    class Meta:
        verbose_name = "Şirket Geliri"
        verbose_name_plural = "Şirket Gelir Listesi"

class CompanyExpenseTable(models.Model):
    table_id = models.BigAutoField(primary_key=True, verbose_name="Tablo Kodu")
    
    def __str__(self):
        return str(self.table_id)
    
    class Meta:
        verbose_name = "Şirket Gider Girişi"
        verbose_name_plural = "Şirket Giderleri"

class CompanyExpense(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    expense_id = models.BigAutoField(primary_key=True, verbose_name="Gelir ID")
    expense_code = models.CharField("Gider Kodu", max_length=8, default=generate_unique_code)
    expense_name = models.CharField("Gider Adı", max_length=100, blank=False, null=False)
    amount = models.DecimalField("Miktar", blank=False, null=False, max_digits=20, decimal_places=2)
    unit_id = models.ForeignKey(UnitName, related_name="company_expense_units", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Birim")
    currency_price = models.DecimalField("Döviz Fiyatı", blank=False, null=False, max_digits=20, decimal_places=2, default=0.00)
    currency_type = models.CharField("Döviz Cinsi", max_length=15, choices=MONEY_UNIT, default=MONEY_UNIT[0][0])
    price = models.DecimalField("Fiyat", max_digits=25, decimal_places=2, blank=False, null=False)
    subtotal = models.DecimalField("Ara Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    vat_rate = models.IntegerField("KDV Oranı (%)", default=0, blank=False, null=False)
    vat_amount = models.DecimalField("KDV Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField("Genel Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    payment_type = models.CharField("Gider Türü", max_length=200, blank=False, null=False, default=PAYMENT_TYPE[0][0], choices=PAYMENT_TYPE)
    table_id = models.ForeignKey(CompanyExpenseTable, on_delete=models.CASCADE, verbose_name="Giriş Bilgisi", editable=False, blank=True, null=True)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))
    expense_to = models.CharField("Kime/Nereye", max_length=200, blank=False, null=False)

    def save(self):
        if self.pk is None:
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = Decimal(CurrencyRates().get_rate('TRY','TRY'))
            elif currency_type == MONEY_UNIT[1][0]:
                default = Decimal(CurrencyRates().get_rate('EUR','TRY'))
            elif currency_type == MONEY_UNIT[2][0]:
                default = Decimal(CurrencyRates().get_rate('USD','TRY'))
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        else:
            self.price = 0
            self.subtotal = 0
            self.vat_amount = 0
            self.grand_total = 0
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = get_curenncy_rates('TRY', self.log_date)
            elif currency_type == MONEY_UNIT[1][0]:
                default = get_curenncy_rates('EUR', self.log_date)
            elif currency_type == MONEY_UNIT[2][0]:
                default = get_curenncy_rates('USD', self.log_date)
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        return super(CompanyExpense, self).save()

    def delete(self, *args, **kwargs):
        Incentive.objects.filter(incentive_code = self.expense_code).delete()
        AdvancePayment.objects.filter(payment_code = self.expense_code).delete()
        SalaryInfo.objects.filter(salary_info_code = self.expense_code).delete()
        Comission.objects.filter(comission_code = self.expense_code).delete()
        PersonalIncome.objects.filter(income_code = self.expense_code).delete()
        PersonalExpenseForUserEntry.objects.filter(expense_code = self.expense_code).update(
            approval_status = APPROVAL_STATUS[0][0],
            payment_status = PAYMENT_STATUS[0][0]
        )
        PersonalExpense.objects.filter(expense_code = self.expense_code).delete()
        CompanyExpense.objects.filter(expense_code = self.expense_code).delete()
        super(CompanyExpense, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.expense_code) + " " + str(self.expense_name)

    class Meta:
        verbose_name = "Şirket Gideri"
        verbose_name_plural = "Şirket Gider Listesi"

class PersonalIncomeSummary(PersonalIncome):
    class Meta:
        proxy = True
        verbose_name = 'Bireysel Gelir Özeti'
        verbose_name_plural = 'Bireysel Gelir Özeti'

class PersonalExpenseSummary(PersonalExpense):
    class Meta:
        proxy = True
        verbose_name = 'Bireysel Gider Özeti'
        verbose_name_plural = 'Bireysel Gider Özeti'

class CompanyIncomeSummary(CompanyIncome):
    class Meta:
        proxy = True
        verbose_name = 'Şirket Gelir Özeti'
        verbose_name_plural = 'Şirket Gelir Özeti'

class CompanyExpenseSummary(CompanyExpense):
    class Meta:
        proxy = True
        verbose_name = 'Şirket Gider Özeti'
        verbose_name_plural = 'Şirket Gider Özeti'

class PersonalExpenseForUserEntry(models.Model):
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    expense_id = models.BigAutoField(primary_key=True, verbose_name="Gider ID")
    expense_code = models.CharField("Gider Kodu", max_length=8, default=generate_unique_code)
    expense_name = models.CharField("Gider Adı", max_length=100, blank=False, null=False)
    amount = models.DecimalField("Miktar", blank=False, null=False, max_digits=20, decimal_places=2)
    unit_id = models.ForeignKey(UnitName, related_name="expense_for_user_entry_units", on_delete=models.CASCADE, null=True, blank=True, verbose_name="Birim")
    currency_price = models.DecimalField("Döviz Fiyatı", blank=False, null=False, max_digits=20, decimal_places=2, default=0.00)
    currency_type = models.CharField("Döviz Cinsi", max_length=15, choices=MONEY_UNIT, default=MONEY_UNIT[0][0])
    price = models.DecimalField("Fiyat", max_digits=25, decimal_places=2, blank=False, null=False)
    subtotal = models.DecimalField("Ara Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    vat_rate = models.IntegerField("KDV Oranı (%)", default=0, blank=False, null=False)
    vat_amount = models.DecimalField("KDV Tutarı", max_digits=25, decimal_places=2, blank=False, null=False)
    grand_total = models.DecimalField("Genel Toplam", max_digits=25, decimal_places=2, blank=False, null=False)
    user = models.CharField("Personel", max_length=50, default=usr)
    log_date = models.DateField("İşlem Tarihi", default=dt.date(dt.now()))
    approval_status = models.CharField("Onay Durumu", max_length=50, blank=False, null=False, choices= APPROVAL_STATUS, default=APPROVAL_STATUS[0][0])
    payment_status = models.CharField("Ödeme Durumu", max_length=120, blank=False, null=False, choices=PAYMENT_STATUS, default=PAYMENT_STATUS[0][0])
    
    def save(self, *args, **kwargs):
        if self.pk is None:
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = Decimal(CurrencyRates().get_rate('TRY','TRY'))
            elif currency_type == MONEY_UNIT[1][0]:
                default = Decimal(CurrencyRates().get_rate('EUR','TRY'))
            elif currency_type == MONEY_UNIT[2][0]:
                default = Decimal(CurrencyRates().get_rate('USD','TRY'))
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
        else:
            self.price = 0
            self.subtotal = 0
            self.vat_amount = 0
            self.grand_total = 0
            currency_type = self.currency_type
            if currency_type == MONEY_UNIT[0][0]:
                default = get_curenncy_rates('TRY', self.log_date)
            elif currency_type == MONEY_UNIT[1][0]:
                default = get_curenncy_rates('EUR', self.log_date)
            elif currency_type == MONEY_UNIT[2][0]:
                default = get_curenncy_rates('USD', self.log_date)
            self.price = self.currency_price * default
            self.subtotal = self.price * self.amount
            self.vat_amount = self.subtotal * (Decimal(self.vat_rate)/100)
            self.grand_total = self.subtotal + self.vat_amount
            if (self.approval_status == 'Onay'):
                try:
                    with transaction.atomic():
                        PersonalExpense.objects.get(expense_code = self.expense_code)
                        PersonalExpense.objects.filter(expense_code = self.expense_code).update(
                            amount = self.amount,
                            unit_id = self.unit_id, 
                            currency_price = self.currency_price,
                            currency_type = self.currency_type,
                            price = self.price,
                            subtotal = self.subtotal,
                            vat_rate = self.vat_rate,
                            vat_amount = self.vat_amount,
                            grand_total = self.grand_total,                     
                        )
                except PersonalExpense.DoesNotExist:
                    a = PersonalExpense(
                        expense_code = self.expense_code,
                        expense_name = self.expense_name,
                        amount = self.amount,
                        unit_id = self.unit_id, 
                        currency_price = self.currency_price,
                        currency_type = self.currency_type,
                        price = self.price,
                        subtotal = self.subtotal,
                        vat_rate = self.vat_rate,
                        vat_amount = self.vat_amount,
                        grand_total = self.grand_total,
                        user = self.user,
                        log_date = self.log_date,                        
                    )
                    a.save()
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, e)
            if (self.payment_status == 'Odendi' and self.approval_status == 'Onay'):
                try:
                    with transaction.atomic():
                        CompanyExpense.objects.get(expense_code = self.expense_code)
                        PersonalIncome.objects.get(income_code = self.expense_code)
                        CompanyExpense.objects.filter(expense_code = self.expense_code).update(
                            amount = self.amount,
                            unit_id = self.unit_id,
                            currency_price = self.currency_price,
                            currency_type = self.currency_type,
                            price = self.price,
                            subtotal = self.subtotal,
                            vat_rate = self.vat_rate,
                            vat_amount = self.vat_amount,
                            grand_total = self.grand_total,
                        )
                        PersonalIncome.objects.filter(income_code = self.expense_code).update(
                            amount = self.amount,
                            unit_id = self.unit_id,
                            currency_price = self.currency_price,
                            currency_type = self.currency_type,
                            price = self.price,
                            subtotal = self.subtotal,
                            vat_rate = self.vat_rate,
                            vat_amount = self.vat_amount,
                            grand_total = self.grand_total,
                        )
                except (CompanyExpense.DoesNotExist, PersonalIncome.DoesNotExist):
                    b = CompanyExpense(
                        expense_code = self.expense_code,
                        expense_name = self.expense_name,
                        amount = self.amount,
                        unit_id = self.unit_id,
                        currency_price = self.currency_price,
                        currency_type = self.currency_type,
                        price = self.price,
                        subtotal = self.subtotal,
                        vat_rate = self.vat_rate,
                        vat_amount = self.vat_amount,
                        grand_total = self.grand_total,
                        payment_type = PAYMENT_TYPE[0][0],
                        expense_to = self.user
                    )
                    b.save()
                    c = PersonalIncome(
                        income_code = self.expense_code,
                        income_name = self.expense_name,
                        amount = self.amount,
                        unit_id = self.unit_id,
                        currency_price = self.currency_price,
                        currency_type = self.currency_type,
                        price = self.price,
                        subtotal = self.subtotal,
                        vat_rate = self.vat_rate,
                        vat_amount = self.vat_amount,
                        grand_total = self.grand_total,
                        user = self.user,
                    )
                    c.save()
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, e)
        return super(PersonalExpenseForUserEntry, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        PersonalExpense.objects.filter(expense_code = self.expense_code).delete()
        CompanyExpense.objects.filter(expense_code = self.expense_code).delete()
        PersonalIncome.objects.filter(income_code = self.expense_code).delete()
        PersonalExpenseForUserEntry.objects.filter(expense_code = self.expense_code).delete()
        super(PersonalExpenseForUserEntry, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.expense_code)

    class Meta:
        verbose_name = "Bireysel Gider Girişi"
        verbose_name_plural = "Bireysel Gider Girişleri"
