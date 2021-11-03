from typing import ValuesView
from django.db import models, transaction
from datetime import datetime
from django.db.models.deletion import CASCADE
import sys, os
import string
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.crypto import get_random_string
from django.core.validators import RegexValidator

from GeneralModel.models import Firm, FirmAuthorizedPerson, DeliveryCompany

##########################################
##########    OTHER MODELS    ############
########################################## 

MONEY_UNIT = [
    ('TRY','TRY'),
    ('USD','USD'),
    ('EUR','EUR'),
    ]

class ProductStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True, verbose_name="Ürün Durumu Kodu")
    status = models.CharField("Ürün Durumu", max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.status)

    class Meta:
        verbose_name = "Ürün Durumu"
        verbose_name_plural = "Ürün Durumları"

class ProductCategory(models.Model):
    category_id = models.BigAutoField(primary_key=True, verbose_name="Kategori Kodu")
    category_name = models.CharField("Kategori Adı", max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.category_name)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

class ProductSubCategory(models.Model):
    sub_category_id = models.BigAutoField(primary_key=True, verbose_name="Kategori Kodu")
    sub_category_name = models.CharField("Kategori Adı", max_length=150, blank=False, null=False)
    parent = models.ForeignKey(ProductCategory, related_name='parent_category', on_delete=models.CASCADE, verbose_name='Ana Kategori', blank=True, null=True)

    def __str__(self):
        return str(self.sub_category_name)

    class Meta:
        verbose_name = "Alt Kategori"
        verbose_name_plural = "Alt Kategoriler"

class ArrivalReason(models.Model):
    arrival_id = models.BigAutoField(primary_key=True, verbose_name="Geliş Nedeni Kodu")
    arrival_reason = models.CharField("Geliş Nedeni", max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.arrival_reason)
    
    class Meta:
        verbose_name = "Geliş Nedeni"
        verbose_name_plural = "Geliş Nedenleri"

class DepartureReason(models.Model):
    departure_id = models.BigAutoField(primary_key=True, verbose_name="Gidiş Nedeni Kodu")
    departure_reason = models.CharField("Gidiş Nedeni", max_length=150, blank=False, null=False)

    def __str__(self):
        return str(self.departure_reason)

    class Meta:
        verbose_name = "Gidiş Nedeni"
        verbose_name_plural = "Gidiş Nedenleri"

class WarehouseInfo(models.Model):
    warehouse_id = models.BigAutoField(primary_key=True, verbose_name="Depo Kodu")
    warehouse_location = models.CharField("Lokasyon", max_length=300, blank=False, null=False)
    shelf_info = models.CharField("Raf Bilgisi", max_length=200, blank=False, null=False)
    shelf_no = models.CharField("Raf No", max_length=20)
    shelf_product_x_axis = models.IntegerField("Sütun (Column)", help_text="", blank=False, null=False)
    shelf_product_y_axis = models.IntegerField("Satır (Row)", help_text="", blank=False, null=False)

    def __str__(self):
        return "Raf No: " + str(self.shelf_no) + " - " + str(self.shelf_product_y_axis) + "/" + str(self.shelf_product_x_axis) + " - "  + str(self.shelf_info)

    class Meta:
        verbose_name = "Depo Bilgisi"
        verbose_name_plural = "Depo Bilgileri"



##########################################
##########    INVENTORY CARD    ##########
########################################## 

class InventoryCardImageSet(models.Model):
    image_set_id = models.BigAutoField(primary_key=True, verbose_name="Görsel Set Kodu")
    image_one = models.ImageField("Görsel 1", upload_to="stock_card_images/product {InventoryCard}", blank=False, null=False)
    image_two = models.ImageField("Görsel 2", upload_to="stock_card_images/product {InventoryCard.product_code}", blank=True, null=True)
    image_three = models.ImageField("Görsel 3", upload_to="stock_card_images/product {InventoryCard.product_code}", blank=True, null=True)
    image_four = models.ImageField("Görsel 4", upload_to="stock_card_images/product {InventoryCard.product_code}", blank=True, null=True)

    def __str__(self):
        return str(self. image_set_id) 

    class Meta:
        verbose_name = ("Görsel Seti")
        verbose_name_plural = ("Görsel Setleri")

class InventoryCard(models.Model):
    card_id = models.BigAutoField(primary_key=True, verbose_name="Kart Kodu")
    product_code = models.CharField("Ürün Kodu", max_length=1000, blank=True, null=True)
    product_name = models.CharField("Ürün Adı", max_length=1000, blank=True, null=True)
    product_category = models.ForeignKey(ProductCategory, related_name="categories", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kategori")
    sub_category = models.ForeignKey(ProductSubCategory, related_name="sub_categories", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Alt Kategori")
    technical_info = models.TextField("Teknik Bilgiler", blank=True, null=True)
    datasheet_document = models.FileField("Datasheet", upload_to="PRODUCT DATASHEETS", null=True, blank=True)
    #image_set = models.ForeignKey(InventoryCardImageSet, related_name="ic_images", blank=True, null=True, verbose_name="Görsel Seti", on_delete=models.CASCADE)
    image_one = models.ImageField("Görsel 1", upload_to="InventoryCard/Images", blank=True, null=True)
    image_two = models.ImageField("Görsel 2", upload_to="InventoryCard/Images", blank=True, null=True)
    image_three = models.ImageField("Görsel 3", upload_to="InventoryCard/Images", blank=True, null=True)
    image_four = models.ImageField("Görsel 4", upload_to="InventoryCard/Images", blank=True, null=True)

    def __str__(self):
        return str(self.product_code) + " " + str(self.product_name)   

    class Meta:
        verbose_name = ("Stok Kartı")
        verbose_name_plural = ("Stok Kartları")


##########################################
###########     INVENTORY     ############
##########################################

class ProductIdentificationImages(models.Model):
    image_set_id = models.BigAutoField(primary_key=True, verbose_name="Görsel Set Kodu")
    image_one = models.ImageField("Görsel 1", upload_to="product_identification_images/product {Inventory.product_code}", blank=True, null=True)
    image_two = models.ImageField("Görsel 2", upload_to="product_identification_images/product {Inventory.product_code}", blank=True, null=True)
    image_three = models.ImageField("Görsel 3", upload_to="product_identification_images/product {Inventory.product_code}", blank=True, null=True)
    image_four = models.ImageField("Görsel 4", upload_to="product_identification_images/product {Inventory.product_code}", blank=True, null=True)

    def __str__(self):
        return str(self.image_set_id)

    class Meta:
        verbose_name = "Ek Numara Ürün Görseli"
        verbose_name_plural = "Ek Numara Ürün Görselleri"




##########################################
##########    PRODUCT ENTRY    ###########
########################################## 

class QuantityCache(models.Model):
    object_id = models.CharField("ID of the Object", max_length=200, blank=False, null=False)
    previous_quantity = models.CharField("Previous Quantity of the Object", max_length=8000,  blank=False, null=False)

    def __str__(self):
        return str(self.object_id) + " " + str(self.previous_quantity)

    class Meta:
        verbose_name = "Quantity Cache"
        verbose_name_plural = "Quantity Caches"

class ProductEnrty(models.Model):
    def user_directory_path(instance, filename):
        return 'PRODUCT SYSTEM DOCUMENTS/{0}/{1}'.format(instance.product_id.product_code, filename)
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    entry_id = models.BigAutoField(primary_key=True, verbose_name="Giriş Kodu")
    unicode = models.CharField("Unicode", max_length=200, editable=False, default=get_random_string)
    #product_id = models.ForeignKey(InventoryCard, related_name="product_entry", on_delete=models.CASCADE, verbose_name="Stok Kartı")
    arrival_reason = models.ForeignKey(ArrivalReason, related_name="arrival_reasons", on_delete=models.CASCADE, verbose_name="Geliş Nedeni")
    date_arrival = models.DateField("İşlem Tarihi", default=datetime.date(datetime.now()))
    date_interval = models.IntegerField("Ne Kadar Duracak", default=0)
    quantity = models.IntegerField("Adet", blank=False, null=False, default=1)
    purchase_price = models.DecimalField("Fiyat", blank=False, null=False, max_digits=20, decimal_places=2)
    money_unit = models.CharField("Para Birimi", max_length=10, default=MONEY_UNIT[0][0], choices=MONEY_UNIT, blank=True, null=True)
    description = models.TextField("Açıklama", blank=False, null=False, default="")
    company = models.ForeignKey(Firm, related_name="entry_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Firma")
    company_authorized = models.ManyToManyField(FirmAuthorizedPerson, related_name="entry_company_authorizeds", blank=True, null=True, verbose_name="Firma Yetkilisi")
    delivery_company = models.ForeignKey(DeliveryCompany, related_name="entry_delivery_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kargo Firmasi")
    delivery_code = models.CharField("Teslimat Kodu", max_length=100, blank=True, null=True)
    delivery_warehouse_receipt_document = models.FileField("Ambar Tesellum Fisi", upload_to="ProductSystem/DeliveryDocs/", blank=True, null=True)
    def __str__(self):
        return str(self.date_arrival)

    class Meta:
        verbose_name = ("Ürün Girişi")
        verbose_name_plural = ("Ürün Girişleri")

##########################################
##########    PRODUCT OUTLET    ##########
########################################## 

class Inventory(models.Model):
    product_id = models.ForeignKey(InventoryCard, related_name="inventory_entry", on_delete=models.CASCADE, verbose_name="Stok Kartı", blank=True, null=True)
    product_code = models.CharField("Kod", max_length=200, unique=False)
    product_name = models.CharField("Cihaz Adı", max_length=1000, blank=True, null=True)
    product_category = models.CharField("Kategori", max_length=300, blank=True, null=True)
    product_sub_category = models.CharField("Alt Kategori", max_length=300, blank=True, null=True)
    category_image = models.ImageField("Gorsel", editable=False, blank=True, null=True, upload_to='InventoryCard/Images')
    recommended_price = models.DecimalField("Tavsiye Edilen Birim Fiyatı", max_digits=20, decimal_places=2, blank=True,null=True)
    money_unit = models.CharField("Para Birimi", max_length=10, default=MONEY_UNIT[0][0], choices=MONEY_UNIT, blank=True, null=True)
    warehouse_info = models.ForeignKey(WarehouseInfo, related_name="ids_warehouse_infos", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Depo Bilgileri")
    product_quantity = models.IntegerField("Miktar", default=1, blank=True,null=True)
    warehouse_location = models.CharField("Lokasyon", max_length=300, blank=True, null=True)
    shelf_info = models.CharField("Raf Bilgisi", max_length=200, blank=True, null=True)
    shelf_no = models.CharField("Raf No", max_length=20, blank=True, null=True)
    shelf_product_x_axis = models.IntegerField("Sütun (Column)", help_text="", blank=True, null=True)
    shelf_product_y_axis = models.IntegerField("Satır (Row)", help_text="", blank=True, null=True)
    inventory_checked = models.BooleanField("Kayıt Tamamlandı", default=False)
    tested_status = models.BooleanField("Test Edildi", default=False)
    test_result_description = models.TextField("Test Açıklaması", blank=True, null=True)
    description = models.TextField("Açıklama", blank=True, null=True)
    product_entry = models.ForeignKey(ProductEnrty, on_delete=models.CASCADE, blank=True, null=True, related_name='inventory_entry', editable=False)
    def save(self, *args, **kwargs):
        product = self.product_id
        #print(product)
        #print(str(product.product_code) + "\n" +  str(product.product_name))
        pro_code = product.product_code
        pro_name = product.product_name
        check = product.product_category
        check2 = product.sub_category
        pro_category = ''
        pro_sub_category = ''

        if check is None:
            pro_category = '-'
        else:
            pro_category = product.product_category.category_name
        
        if check2 is None:
            pro_sub_category = '-'
        else:
            pro_sub_category = product.sub_category.sub_category_name


        print('Inventory Image Path: {0}'.format(product.image_one))
        print('INVENTORY - PRODUCT CODE: {0}'.format(pro_code))
        print('INVENTORY - PRODUCT NAME: {0}'.format(pro_name))
        try:
            if pro_category is None:
                if self.pk is None:
                    self.product_code = pro_code
                    self.product_name = pro_name
                    self.product_category = "-"
                    self.category_image = product.image_one
                else:
                    self.product_code = pro_code
                    self.product_name = pro_name
                    self.product_category = "-"
                    self.category_image = product.image_one
            else:
                if self.pk is None:
                    self.product_code = pro_code
                    self.product_name = pro_name
                    self.product_category = pro_category
                    self.category_image = product.image_one
                else:
                    self.product_code = pro_code
                    self.product_name = pro_name
                    self.product_category = pro_category
                    self.category_image = product.image_one
            
            if pro_sub_category is None:
                if self.pk is None:
                    self.product_sub_category = "-"
                else:
                    self.product_sub_category = "-"
            else:
                if self.pk is None:
                    self.product_sub_category = pro_sub_category
                else:
                    self.product_sub_category = pro_sub_category

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print('Invetory Save Method - PK NOT NULL: {0}\n{1}\n{2}\n{3}'.format(exc_type, fname, exc_tb.tb_lineno, e))

        super(Inventory, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.product_code) + " " + str(self.product_name)

    class Meta:
        verbose_name = ("Envanter Kaydı")
        verbose_name_plural = ("Envanter")
    #     permissions = [
    #         ('edit_inventory_warehouse_location', 'DENEME EDIT PERMISSION'),
    #     ]
        permissions = [
            ('custom_permission', 'Custom View Permission')
        ]

class ProductIdentification(models.Model):
    additional_serial = models.CharField("Seri No",unique=False,default='', blank=False,null=False, max_length=30)
    additional_internal = models.CharField("Dahili No",unique=False, blank=False, null=False, max_length=30)
    product_status = models.ForeignKey(ProductStatus, related_name="product_status", on_delete=models.CASCADE, verbose_name="Ürün Durumu")
    additional_description = models.TextField("Açıklama", blank=False, null=False)
    tested_status = models.BooleanField("Test Edildi", default=False)
    test_result_description = models.TextField("Test Açıklaması", blank=True, null=True)
    product_id = models.ForeignKey(Inventory, on_delete=models.CASCADE, related_name="id_images")
    image_one = models.ImageField("Görsel 1", upload_to="InventoryID/Images", blank=True, null=True)
    image_two = models.ImageField("Görsel 2", upload_to="InventoryID/Images", blank=True, null=True)
    image_three = models.ImageField("Görsel 3", upload_to="InventoryID/Images", blank=True, null=True)
    image_four = models.ImageField("Görsel 4", upload_to="InventoryID/Images", blank=True, null=True)

    def __str__(self):
        return "DAHİLİ NO: " + str(self.additional_internal)

    class Meta:
        verbose_name = ("Urun Kimligi")
        verbose_name_plural = ("Urun Kimlikleri")

class InventoryImages(models.Model):
    image_set_id = models.BigAutoField(primary_key=True, verbose_name="Görsel Set Kodu")
    inventory_id = models.ForeignKey(Inventory, related_name="inventory_ids", on_delete=models.CASCADE, verbose_name="Stok Kartı")
    image_one = models.ImageField("Görsel 1", upload_to="stock_card_images/product {Inventory.product_code}", blank=True, null=True)
    image_two = models.ImageField("Görsel 2", upload_to="stock_card_images/product {Inventory.product_code}", blank=True, null=True)
    image_three = models.ImageField("Görsel 3", upload_to="stock_card_images/product {Inventory.product_code}", blank=True, null=True)
    image_four = models.ImageField("Görsel 4", upload_to="stock_card_images/product {Inventory.product_code}", blank=True, null=True)

    def __str__(self):
        return str(self.image_set_id)

    class Meta: 
        verbose_name = "Envanter Görseli"
        verbose_name_plural = "Envanter Görselleri"

'''
class ProductOutlet(models.Model):
    def user_directory_path(instance, filename):
        return 'PRODUCT SYSTEM DOCUMENTS/{0}/{1}'.format(instance.outlet_id, filename)
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    outlet_id = models.BigAutoField(primary_key=True, verbose_name="Çıkış Kodu")
    unicode = models.CharField("Unicode", max_length=1000, editable=False, default=get_random_string)
    has_serial = models.BooleanField('Dahili no ile ara', blank=True,)
    product_id = models.ManyToManyField(ProductIdentification, related_name="product_outlet_id", verbose_name="Ürün", blank=True, null=True)
    product_id_inv = models.ManyToManyField(Inventory, related_name="product_outlet_id", verbose_name="Ürün", blank=True, null=True)
    departure_reason = models.ForeignKey(DepartureReason, related_name="departure_reasons", on_delete=models.CASCADE, verbose_name="Gidiş Nedeni", blank=True, null=True)
    date_departure = models.DateField("İşlem Tarihi", default=datetime.date(datetime.now()), blank=True, null=True)
    date_interval = models.IntegerField("Ne Kadar Duracak", default=0, blank=True, null=True)
    quantity = models.IntegerField("Adet", blank=True, null=True, default=1)
    selling_price = models.DecimalField("Fiyat", blank=True, null=True, max_digits=20, decimal_places=2)
    money_unit = models.CharField("Para Birimi", max_length=10, default=MONEY_UNIT[0][0], choices=MONEY_UNIT, blank=True, null=True)
    image = models.ImageField("Görsel", upload_to=user_directory_path, blank=True, null=True)
    image1 = models.ImageField("Görsel 2", upload_to=user_directory_path, blank=True, null=True)
    image2 = models.ImageField("Görsel 3", upload_to=user_directory_path, blank=True, null=True)
    image3 = models.ImageField("Görsel 4", upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField("Açıklama", blank=True, null=True, default="")
    company = models.ForeignKey(Firm, related_name="outlet_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Firma")
    company_authorized = models.ManyToManyField(FirmAuthorizedPerson, related_name="outlet_company_authorizeds", blank=True, null=True, verbose_name="Firma Yetkilisi")
    delivery_company = models.ForeignKey(DeliveryCompany, related_name="outlet_delivery_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kargo Firmasi")
    delivery_code = models.CharField("Teslimat Kodu", max_length=100, blank=True, null=True)
    delivery_warehouse_receipt_document = models.FileField("Ambar Tesellum Fisi", upload_to="ProductSystem/DeliveryDocs/", blank=True, null=True)

    def __str__(self):
        return str(self.outlet_id)

    class Meta:
        verbose_name = "Ürün Çıkışı"
        verbose_name_plural = "Ürün Çıkışları"
'''

class ProductOutlet(models.Model):
    def user_directory_path(instance, filename):
        return 'PRODUCT SYSTEM DOCUMENTS/{0}/{1}'.format(instance.outlet_id, filename)
    def generate_unique_code():
        return get_random_string(8, allowed_chars=string.ascii_uppercase + string.digits)
    outlet_id = models.BigAutoField(primary_key=True, verbose_name="Çıkış Kodu")
    unicode = models.CharField("Unicode", max_length=1000, editable=False, default=get_random_string)
    has_serial = models.BooleanField('Dahili no ile ara', blank=True,)
    product_id = models.ForeignKey(ProductIdentification, related_name="product_outlet_id", verbose_name="Ürün Dahili No", blank=True, null=True, on_delete=models.CASCADE)
    product_id_inv = models.ForeignKey(Inventory, related_name="product_outlet_id", verbose_name="Ürün Adi", blank=True, null=True, on_delete=models.CASCADE)
    departure_reason = models.ForeignKey(DepartureReason, related_name="departure_reasons", on_delete=models.CASCADE, verbose_name="Gidiş Nedeni", blank=True, null=True)
    date_departure = models.DateField("İşlem Tarihi", default=datetime.date(datetime.now()), blank=True, null=True)
    date_interval = models.IntegerField("Ne Kadar Duracak", default=0, blank=True, null=True)
    quantity = models.IntegerField("Adet", blank=True, null=True, default=1)
    selling_price = models.DecimalField("Fiyat", blank=True, null=True, max_digits=20, decimal_places=2)
    money_unit = models.CharField("Para Birimi", max_length=10, default=MONEY_UNIT[0][0], choices=MONEY_UNIT, blank=True, null=True)
    image = models.ImageField("Görsel", upload_to=user_directory_path, blank=True, null=True)
    image1 = models.ImageField("Görsel 2", upload_to=user_directory_path, blank=True, null=True)
    image2 = models.ImageField("Görsel 3", upload_to=user_directory_path, blank=True, null=True)
    image3 = models.ImageField("Görsel 4", upload_to=user_directory_path, blank=True, null=True)
    description = models.TextField("Açıklama", blank=True, null=True, default="")
    company = models.ForeignKey(Firm, related_name="outlet_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Firma")
    company_authorized = models.ManyToManyField(FirmAuthorizedPerson, related_name="outlet_company_authorizeds", blank=True, null=True, verbose_name="Firma Yetkilisi")
    delivery_company = models.ForeignKey(DeliveryCompany, related_name="outlet_delivery_companies", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Kargo Firmasi")
    delivery_code = models.CharField("Teslimat Kodu", max_length=100, blank=True, null=True)
    delivery_warehouse_receipt_document = models.FileField("Ambar Tesellum Fisi", upload_to="ProductSystem/DeliveryDocs/", blank=True, null=True)

    def clean(self, *args, **kwargs):
        errors={}

        product = self.product_id
        if product is None:
            product_ids = self.product_id_inv
            inventory_object = Inventory.objects.get(pk = product_ids.pk)
            current_quantity = inventory_object.product_quantity
            if self.quantity > current_quantity :
                errors['quantity']=ValidationError('Envanterde istenilen sayıda seçilen ürün bulunmamaktadır!')
            if errors:
                raise ValidationError(errors)
        else:
            inventory_object = Inventory.objects.get(pk = product.pk)
            current_quantity = inventory_object.product_quantity
            if self.quantity > current_quantity :
                errors['quantity']=ValidationError('Envanterde istenilen sayıda seçilen ürün bulunmamaktadır!')
            if errors:
                raise ValidationError(errors)

    def save(self, *args, **kwargs):
        product = self.product_id
        if product is None:
            if self.pk is None:
                product_ids = self.product_id_inv
                try: 
                    with transaction.atomic():
                        inventory_object = Inventory.objects.get(pk = product_ids.pk)
                        current_quantity = inventory_object.product_quantity
                        if current_quantity < self.quantity:
                            raise ValueError('Insufficient funds!')
                        else:
                            Inventory.objects.filter(pk = product_ids.pk).update(
                                product_quantity = current_quantity - self.quantity
                            )
                            a = QuantityCache(
                                object_id = self.unicode,
                                previous_quantity = self.quantity
                            )
                            a.save()
                except Inventory.DoesNotExist:
                    raise ValueError('The product does not exists in inventory!')
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, exc_obj, e)
            else:
                product_ids = self.product_id_inv
                try:
                    with transaction.atomic():
                        Inventory.objects.get(pk = product_ids.pk)
                        inventory_object = Inventory.objects.get(pk = product_ids.pk)
                        current_quantity = inventory_object.product_quantity
                        quantity_cache = QuantityCache.objects.get(object_id = self.unicode)
                        prev_quantity = int(quantity_cache.previous_quantity)
                        print(prev_quantity)
                        #if current_quantity < (self.quantity + prev_quantity):
                        #     raise ValueError('Insufficient funds!')
                        # else:
                        Inventory.objects.filter(pk = product_ids.pk).update(
                            product_quantity = current_quantity - self.quantity + prev_quantity
                        )
                        if quantity_cache is None:
                            a = QuantityCache(
                                object_id = self.unicode,
                                previous_quantity = self.quantity
                            )
                            a.save()
                        else:
                            QuantityCache.objects.filter(object_id = self.unicode).update(
                                previous_quantity = self.quantity
                            )

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, e)
        else:
            if self.pk is None:
                try: 
                    with transaction.atomic():
                        inventory_object = Inventory.objects.get(pk = product.pk)
                        current_quantity = inventory_object.product_quantity
                        if current_quantity < self.quantity:
                            raise ValueError('Insufficient funds!')
                        else:
                            Inventory.objects.filter(pk = product.pk).update(
                                product_quantity = current_quantity - self.quantity
                            )
                            a = QuantityCache(
                                object_id = self.unicode,
                                previous_quantity = self.quantity
                            )
                            a.save()
                except Inventory.DoesNotExist:
                    raise ValueError('The product does not exists in inventory!')
                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, exc_obj, e)
            else:
                try:
                    with transaction.atomic():
                        Inventory.objects.get(pk = product.pk)
                        inventory_object = Inventory.objects.get(pk = product.pk)
                        current_quantity = inventory_object.product_quantity
                        quantity_cache = QuantityCache.objects.get(object_id = self.unicode)
                        prev_quantity = int(quantity_cache.previous_quantity)
                        print(prev_quantity)
                        #if current_quantity < (self.quantity + prev_quantity):
                        #     raise ValueError('Insufficient funds!')
                        # else:
                        Inventory.objects.filter(pk = product.pk).update(
                            product_quantity = current_quantity - self.quantity + prev_quantity
                        )
                        if quantity_cache is None:
                            a = QuantityCache(
                                object_id = self.unicode,
                                previous_quantity = self.quantity
                            )
                            a.save()
                        else:
                            QuantityCache.objects.filter(object_id = self.unicode).update(
                                previous_quantity = self.quantity
                            )

                except Exception as e:
                    exc_type, exc_obj, exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno, e)
        super(ProductOutlet, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        product = self.product_id
        if product is None:
            product_ids = self.product_id_inv
            quantity_cache = QuantityCache.objects.get(object_id = self.unicode)
            prev_quantity = int(quantity_cache.previous_quantity)
            inventory_object = Inventory.objects.get(pk = product_ids.pk)
            current_quantity = inventory_object.product_quantity
            Inventory.objects.filter(pk = product_ids.pk).update(
                product_quantity = current_quantity + prev_quantity
            )
            QuantityCache.objects.filter(object_id = self.unicode).delete()
            super(ProductOutlet, self).delete(*args, **kwargs)
        else:
            quantity_cache = QuantityCache.objects.get(object_id = self.unicode)
            prev_quantity = int(quantity_cache.previous_quantity)
            inventory_object = Inventory.objects.get(pk = product.pk)
            current_quantity = inventory_object.product_quantity
            Inventory.objects.filter(pk = product.pk).update(
                product_quantity = current_quantity + prev_quantity
            )
            QuantityCache.objects.filter(object_id = self.unicode).delete()
            super(ProductOutlet, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.outlet_id)

    class Meta:
        verbose_name = "Ürün Çıkışı"
        verbose_name_plural = "Ürün Çıkışları"
        
   
        

        
        
