from django.contrib import admin
from ProductSystem.models import *
from django.utils.safestring import mark_safe
from django.forms import TextInput, Textarea
from ProductSystem.resources import InventoryCardResource, InventoryResource
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Permission, User
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class InventoryCardAdmin(ImportExportModelAdmin):
    list_display = (
        'card_id',
        'product_code',
        'product_name',
        'product_category',
        'sub_category',
        'datasheet_document',
        'image_preview1',
    )

    list_display_links = (
        'card_id',
        'product_code',
        'product_name',
        'product_category',
        'sub_category',
        'image_preview1',
    )

    search_fields = (
        'card_id',
        'product_code',
        'product_name',
    )

    list_filter = (
        'product_category',
        'sub_category',
    )
    readonly_fields = ['image_preview1','image_preview2','image_preview3','image_preview4',]

    resource_class = InventoryCardResource
    # fields = (
    #     ('product_code', 'product_name',),
    #     'product_category', 'technical_info',
    #     ('image_one', 'image_two'), ('image_three', 'image_four'),
    #     ('image_preview1','image_preview2','image_preview3','image_preview4'),
    # )

    fieldsets = (
        ('Ürün Bilgileri', {
            'fields': ( ('product_code', 'product_name',),
        ('product_category', 'sub_category'), 'technical_info','datasheet_document',),
        }),
        ('Görsel Yükle', {
            'fields': (('image_one', 'image_two'), ('image_three', 'image_four'),),
        }),
        ('Görsel Ön izleme', {
            'fields': (('image_preview1','image_preview2','image_preview3','image_preview4'),),
        }),
    )

    def image_preview1(self, obj):
        # ex. the name of column is "image"
        if obj.image_one:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_one.url))
        else:
            return '(No image)'

    def image_preview2(self, obj):
        # ex. the name of column is "image"
        if obj.image_two:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_two.url))
        else:
            return '(No image)'

    def image_preview3(self, obj):
        # ex. the name of column is "image"
        if obj.image_three:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_three.url))
        else:
            return '(No image)'
    
    def image_preview4(self, obj):
        # ex. the name of column is "image"
        if obj.image_four:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_four.url))
        else:
            return '(No image)'

    image_preview1.short_description = "Ön izleme 1"
    image_preview2.short_description = "Ön izleme 2"
    image_preview3.short_description = "Ön izleme 3"
    image_preview4.short_description = "Ön izleme 4"
  
class ProductIdentificationInline(NestedStackedInline):
    model = ProductIdentification
    fk_name = 'product_id'
    extra = 0
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':3, 'cols':30})},
        models.CharField: {'widget' : TextInput (attrs={'size':20})}

    }
    fieldsets = (
        ('', {
            'fields': (('additional_serial', 'additional_internal'), ('product_status','tested_status'), ('additional_description','test_result_description'),)
        }),
        ('Görseller', {
            'fields': (('image_one', 'image_two'), ('image_three', 'image_four'),),
        }),
        ('', {
            'fields': (('image_preview1','image_preview2','image_preview3','image_preview4'),),
        }),
    )
    readonly_fields = ['image_preview1','image_preview2','image_preview3','image_preview4',]
    
    def image_preview1(self, obj):
        # ex. the name of column is "image"
        if obj.image_one:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_one.url))
        else:
            return '(No image)'

    def image_preview2(self, obj):
        # ex. the name of column is "image"
        if obj.image_two:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_two.url))
        else:
            return '(No image)'

    def image_preview3(self, obj):
        # ex. the name of column is "image"
        if obj.image_three:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_three.url))
        else:
            return '(No image)'
    
    def image_preview4(self, obj):
        # ex. the name of column is "image"
        if obj.image_four:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_four.url))
        else:
            return '(No image)'
    image_preview1.short_description = "Ön izleme 1"
    image_preview2.short_description = "Ön izleme 2"
    image_preview3.short_description = "Ön izleme 3"
    image_preview4.short_description = "Ön izleme 4"

    

class InventoryAdmin(admin.ModelAdmin):
    #resource_class = InventoryResource
    inlines = [ProductIdentificationInline,]
    raw_id_fields = ('product_id',)
    list_display = (
        'product_code',
        'product_name',
        'product_category',
        'product_sub_category',
        'product_quantity',
        'recommended_price',
        'money_unit',
        'inventory_checked',
        'description',
        'category_image_preview'
        #'tested_status',
        # 'warehouse_info',
        # 'additional_serials',
        # 'additional_internals',
    )

    # raw_id_fields = ('additional_number',)

    fieldsets = (
        ('Envanter Bilgisi', {
            'fields': (('product_id','product_code', 'product_name'), ('product_category', 'product_sub_category', 'category_image_preview'), ('recommended_price','money_unit'), 'inventory_checked','product_quantity', 'description',)
        }),
        ('', {
            'fields': (('warehouse_location', 'shelf_info'), ('shelf_no', 'shelf_product_x_axis', 'shelf_product_y_axis'),)
        }),
        # ('Ürün Kimlik Bilgileri', {
        #     'fields': ('additional_number',),
        # }),
    )

    list_display_links = (
        'product_code',
        'product_name',
        'product_quantity',
        #'warehouse',
        # 'inventory_checked',
        # 'additional_serials',
        # 'additional_internals',
    )
    
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':3, 'cols':30})},
        models.CharField: {'widget' : TextInput(attrs={'size':30})}

    }

    search_fields = (
        'product_code',
        'product_name',
        'id_images__additional_internal',
        'id_images__additional_serial',
        #'warehouse',
        'inventory_checked',
        'description',
        # 'additional_serials',
        # 'additional_internals',
        # 'additional_numbers'
    )
    show_change_link = True
    list_filter = (
        #'warehouse',
        'inventory_checked',
        'product_category',
        'product_sub_category'
    )
    list_editable = ('recommended_price', 'description', 'money_unit')
    #resource_class = InventoryResource
    readonly_fields = ('product_code', 'product_name', 'product_category', 'product_sub_category', 'category_image_preview')

    def category_image_preview(self, obj):
        if obj.category_image:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.category_image.url))
        else:
            return '(No image)'

    category_image_preview.short_description = "Gorsel"

    def get_form(self, request, obj=None, **kwargs):
        print('INVENTORY PERMISSION: {0}'.format(request.user.has_perm('ProductSystem.custom_permission')))
        if request.user.has_perm('ProductSystem.custom_permission'):
            self.fieldsets[0][1]["fields"] = (('product_id','product_code', 'product_name'), ('product_category', 'product_sub_category', 'category_image_preview'), ('recommended_price','money_unit'), 'inventory_checked','product_quantity', 'description',)
            self.fieldsets[1][1]["fields"] = (('warehouse_location', 'shelf_info'), ('shelf_no', 'shelf_product_x_axis', 'shelf_product_y_axis'),)
            self.inlines[0].fieldsets[0][1]["fields"] = (('additional_serial', 'additional_internal'), ('product_status','tested_status'), ('additional_description','test_result_description'),)
            self.inlines[0].fieldsets[1][1]["fields"] = (('image_one', 'image_two'), ('image_three', 'image_four'),)
            self.inlines[0].fieldsets[2][1]["fields"] = (('image_preview1','image_preview2','image_preview3','image_preview4'),)
            form = super(InventoryAdmin,self).get_form(request, obj, **kwargs)
            
        else:
            #self.exclude = ('warehouse_location','shelf_info', 'shelf_no', 'shelf_product_x_axis', 'shelf_product_y_axis','inventory_checked',)
            #self.inlines[0].exclude = ('tested_status', 'test_result_description', 'image_one', 'image_two', 'image_three', 'image_four','additional_serial',)
            ## Dynamically overriding
            self.fieldsets[0][1]["fields"] = (('product_id','product_code', 'product_name'), ('product_category', 'product_sub_category', 'category_image_preview'), ('recommended_price','money_unit'), 'product_quantity', 'description',)
            self.fieldsets[1][1]["fields"] = ()
            self.inlines[0].fieldsets[0][1]["fields"] =(('additional_internal'), ('product_status'), ('additional_description',),)
            self.inlines[0].fieldsets[1][1]['fields'] = ''
            #self.inlines[0].fieldsets[1] = ('Görsel Yükle', {'fields': ()})
            self.inlines[0].fieldsets[2][1]["fields"] = (('image_preview1','image_preview2','image_preview3','image_preview4'),)
            form = super(InventoryAdmin,self).get_form(request, obj, **kwargs)
        return form
    
    def get_list_display(self, request):
        if request.user.has_perm('ProductSystem.custom_permission'):
            return self.list_display
        else:
            custom_list = (
                'product_code',
                'product_name',
                'product_category',
                'product_sub_category',
                'product_quantity',
                'recommended_price',
                'money_unit',
                'description',
                'category_image_preview'
            )
            return custom_list
    
    def get_list_filter(self, request):
        if request.user.has_perm('ProductSystem.custom_permission'):
            return self.list_filter
        else:
            custom_list = (
                'product_category',
                'product_sub_category'
            )
            return custom_list

    def get_queryset(self, request):
        from django.db.models import Q
        qs = super(InventoryAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.has_perm('ProductSystem.custom_permission'):
            return qs        
        return qs.filter(~Q(product_category = 'Handcrafts'))

    # def get_form(self, request, obj=None, **kwargs):
    #     print('ID INLINE PERMISSION: {0}'.format(request.user.has_perm('ProductSystem.custom_permission')))
    #     if request.user.has_perm('ProductSystem.custom_permission'):
    #         self.fieldsets[0][1]["fields"] = (('additional_serial', 'additional_internal'), ('product_status','tested_status'), ('additional_description','test_result_description'),)
    #         self.fieldsets[1][1]["fields"] = (('image_one', 'image_two'), ('image_three', 'image_four'),),
    #         self.fieldsets[2][1]["fields"] = (('image_preview1','image_preview2','image_preview3','image_preview4'),),
    #         form = super(ProductIdentificationInline,self).get_form(request, obj, **kwargs)
    #         return form 
    #     else:
    #         self.exclude = ('tested_status', 'test_result_description', 'image_one', 'image_two', 'image_three', 'image_four')
    #         ## Dynamically overriding
    #         self.fieldsets[0][1]["fields"] = (('additional_serial', 'additional_internal'), ('product_status'), ('additional_description',),)
    #         self.fieldsets[1][1]["fields"] = ()
    #         self.fieldsets[2][1]["fields"] = (('image_preview1','image_preview2','image_preview3','image_preview4'),),
    #         form = super(ProductIdentificationInline,self).get_form(request, obj, **kwargs)
    #         return form  
    #filter_horizontal = ('additional_number',)

    # def additional_serials(self, obj):
    #     return ", ".join({p.additional_serial for p in obj.additional_number.all()})
    # additional_serials.short_description = "Seri Numaraları"

    # def additional_internals(self, obj):
    #     return ", ".join({p.additional_internal for p in obj.additional_number.all()})
    # additional_internals.short_description = "Dahili Numaraları"

class InventoryInline(NestedStackedInline):
    fk_name = 'product_entry'
    model = Inventory
    max_num = 1
    inlines = [ProductIdentificationInline]
    raw_id_fields = ('product_id',)

    # raw_id_fields = ('additional_number',)

    fieldsets = (
        ('Envanter Bilgisi', {
            'fields': (('product_id', 'product_name', 'product_code'),('product_category', 'product_sub_category', 'category_image_preview'), ('recommended_price','money_unit'), 'inventory_checked','product_quantity', 'description',)
        }),
        ('', {
            'fields': (('warehouse_location', 'shelf_info'), ('shelf_no', 'shelf_product_x_axis', 'shelf_product_y_axis'),)
        }),
        # ('Ürün Kimlik Bilgileri', {
        #     'fields': ('additional_number',),
        # }),
    )
    
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':3, 'cols':30})},
        models.CharField: {'widget' : TextInput(attrs={'size':30})}

    }
    list_editable = ('recommended_price', 'description', 'money_unit')
    #resource_class = InventoryResource
    readonly_fields = ('product_code', 'product_name', 'product_category', 'product_sub_category', 'category_image_preview')

    def category_image_preview(self, obj):
        if obj.category_image:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.category_image.url))
        else:
            return '(No image)'

    category_image_preview.short_description = "Gorsel"

class ProductIdentificationAdmin(admin.ModelAdmin):
    list_display = (
        'additional_serial',
        'additional_internal',
        'product_status',
        'additional_description',
        'tested_status',
        'test_result_description',
        'image_preview1',
        'image_preview2',
        'image_preview3',
        'image_preview4'
    )
    list_display_links = (
        'additional_serial',
        'additional_internal',
     
        'additional_description',
        # 'product_codes'
    )
    
    fieldsets = (
        ('', {
            'fields': (('additional_serial', 'additional_internal'), ('product_status','tested_status'), ('additional_description','test_result_description'),)
        }),
        ('Görsel Yükle', {
            'fields': (('image_one', 'image_two'), ('image_three', 'image_four'),),
        }),
        ('Görsel Ön izleme', {
            'fields': (('image_preview1','image_preview2','image_preview3','image_preview4'),),
        }),
    )
    readonly_fields = ['image_preview1','image_preview2','image_preview3','image_preview4',]
    def image_preview1(self, obj):
        # ex. the name of column is "image"
        if obj.image_one:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_one.url))
        else:
            return '(No image)'

    def image_preview2(self, obj):
        # ex. the name of column is "image"
        if obj.image_two:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_two.url))
        else:
            return '(No image)'

    def image_preview3(self, obj):
        # ex. the name of column is "image"
        if obj.image_three:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_three.url))
        else:
            return '(No image)'
    
    def image_preview4(self, obj):
        if obj.image_four:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image_four.url))
        else:
            return '(No image)'

    image_preview1.short_description = "Ön izleme 1"    
    image_preview2.short_description = "Ön izleme 2"
    image_preview3.short_description = "Ön izleme 3"
    image_preview4.short_description = "Ön izleme 4"
    
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        if request.user.has_perm('ProductSystem.custom_permission'):
            return True
        else:
            return False
    def has_delete_permission(self, request, obj=None):
        return False
    # def product_codes(self, obj):
        
    #     return ", ".join({p.product_code for p in additional_id.inventory_additional_ids.all()})
    # product_codes.short_description = "Ürün Kodu"




class ProductEntryAdmin(NestedModelAdmin):
    inlines = [InventoryInline]
    raw_id_fields = ('company',)
    #autocomplete_fields = ['product_id', 'company', 'delivery_company']
    list_display = (
        #'product_id',
        'product_name',
        'product_code',
        'product_category',
        'arrival_reason',
        'quantity',
        'purchase_price',
        'money_unit',
        'date_arrival',
        'date_interval',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        
        # 'deliverer'
    )
    def product_name(self, obj):
        return ", ".join([
            str(child.product_name) for child in obj.inventory_entry.all()
        ])
    product_name.short_description = "Urun Adi"

    def product_code(self, obj):
        return ", ".join([
            child.product_code for child in obj.inventory_entry.all()
        ])
    
    product_code.short_description = "Urun Kodu"

    def product_category(self, obj):
        return ", ".join([
            child.product_category for child in obj.inventory_entry.all()
        ])
    product_category.short_description = "Kategori"

    filter_horizontal = ('company_authorized',)
    #filter_vertical = ('deliverer', 'company_authorized')
    list_display_links = (
        #'product_id',
        'product_name',
        'product_code',
        'product_category',
        'arrival_reason',
        'date_arrival',
        'date_interval',
        'quantity',
        'purchase_price',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    search_fields = (
        'description',
        # 'company_authorized',
        # 'deliverer'
    )
    
    fieldsets = (
        ('Giris Bilgeri', {
            'fields': (('arrival_reason'), ('date_arrival','date_interval'),('purchase_price','money_unit',), 'quantity','description',)
        }),

        ('Firma Bilgileri', {
            'classes': ('collapse',),
            'fields': (('company', 'company_authorized'),)
        }),
        ('Teslimat Bilgileri', {
            'classes': ('collapse',),
            'fields': (('delivery_company', 'delivery_code', 'delivery_warehouse_receipt_document'),)
        }),
    )

    list_filter = ( 
        'arrival_reason',
    )


'''class ProductOutletAdmin(admin.ModelAdmin):
    raw_id_fields = ['product_id', 'company', 'delivery_company',]
    filter_horizontal = ['company_authorized', 'deliverer']
    list_display = (
        'product_id',
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    list_display_links = (
        'product_id',
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    search_fields = (
        'description',
        # 'company_authorized',
        # 'deliverer'
    )

    list_filter = (
        'departure_reason',
    )
    fieldsets = (
        ('Giris Bilgeri', {
            'fields': (('product_id', 'departure_reason'), ('date_departure','date_interval'),('selling_price','money_unit',), 'quantity','description', ('image','image1'),('image2','image3'))
        }),
        ('Firma Bilgileri', {
            'fields': (('company', 'company_authorized'),)
        }),
        ('Teslimat Bilgileri', {
            'fields': (('delivery_company', 'deliverer'),)
        }),
    )
'''
'''
class ProductOutletAdmin(admin.ModelAdmin):
    raw_id_fields = ['company',]
    filter_horizontal = ['company_authorized', 'product_id', 'product_id_inv']
    list_display = (
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image_preview1',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    list_display_links = (
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image_preview1',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    search_fields = (
        'description',
        # 'company_authorized',
        # 'deliverer'
    )

    list_filter = (
        'departure_reason',
    )
    readonly_fields = ('image_preview1','image_preview2', 'image_preview3', 'image_preview4')
    fieldsets = (
        ('Cikis Bilgeri', {
            'fields': ('has_serial','product_id','product_id_inv','departure_reason', ('date_departure','date_interval'),('selling_price','money_unit',), 'quantity','description')
        }),
        ('Görsel Yükle', {
            'fields': (('image', 'image1'), ('image2', 'image3'),),
        }),
        ('Görsel Ön izleme', {
            'fields': (('image_preview1','image_preview2','image_preview3','image_preview4'),),
        }),
        ('Firma Bilgileri', {
            'fields': (('company', 'company_authorized'),)
        }),
        ('Teslimat Bilgileri', {
            'fields': (('delivery_company', 'delivery_code', 'delivery_warehouse_receipt_document'),)
        }),
    )

    def image_preview1(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image.url))
        else:
            return '(No image)'

    def image_preview2(self, obj):
        # ex. the name of column is "image"
        if obj.image1:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image1.url))
        else:
            return '(No image)'

    def image_preview3(self, obj):
        # ex. the name of column is "image"
        if obj.image2:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image2.url))
        else:
            return '(No image)'
    
    def image_preview4(self, obj):
        # ex. the name of column is "image"
        if obj.image3:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image3.url))
        else:
            return '(No image)'
    image_preview1.short_description = "Ön izleme 1"
    image_preview2.short_description = "Ön izleme 2"
    image_preview3.short_description = "Ön izleme 3"
    image_preview4.short_description = "Ön izleme 4"

    class Media:
        js = ('/static/admin/js/hide_attribute.js',)
'''

class ProductOutletAdmin(admin.ModelAdmin):
    raw_id_fields = ['company', 'product_id', 'product_id_inv']
    filter_horizontal = ['company_authorized',]
    list_display = (
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image_preview1',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    list_display_links = (
        'departure_reason',
        'date_departure',
        'date_interval',
        'quantity',
        'selling_price',
        'money_unit',
        'image_preview1',
        'description',
        'company',
        # 'company_authorized',
        'delivery_company',
        # 'deliverer'
    )

    search_fields = (
        'description',
        # 'company_authorized',
        # 'deliverer'
    )

    list_filter = (
        'departure_reason',
    )
    readonly_fields = ('image_preview1','image_preview2', 'image_preview3', 'image_preview4')
    fieldsets = (
        ('Cikis Bilgeri', {
            'fields': ('has_serial','product_id','product_id_inv','departure_reason', ('date_departure','date_interval'),('selling_price','money_unit',), 'quantity','description')
        }),
        ('Görsel Yükle', {
            'fields': (('image', 'image1'), ('image2', 'image3'),),
        }),
        ('Görsel Ön izleme', {
            'fields': (('image_preview1','image_preview2','image_preview3','image_preview4'),),
        }),
        ('Firma Bilgileri', {
            'fields': (('company', 'company_authorized'),)
        }),
        ('Teslimat Bilgileri', {
            'fields': (('delivery_company', 'delivery_code', 'delivery_warehouse_receipt_document'),)
        }),
    )

    def image_preview1(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image.url))
        else:
            return '(No image)'

    def image_preview2(self, obj):
        # ex. the name of column is "image"
        if obj.image1:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image1.url))
        else:
            return '(No image)'

    def image_preview3(self, obj):
        # ex. the name of column is "image"
        if obj.image2:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image2.url))
        else:
            return '(No image)'
    
    def image_preview4(self, obj):
        # ex. the name of column is "image"
        if obj.image3:
            return mark_safe('<a target="_blank" href="{0}"><img src="{0}" width="150" height="150" style="object-fit:contain" /></a>'.format(obj.image3.url))
        else:
            return '(No image)'
    image_preview1.short_description = "Ön izleme 1"
    image_preview2.short_description = "Ön izleme 2"
    image_preview3.short_description = "Ön izleme 3"
    image_preview4.short_description = "Ön izleme 4"

    class Media:
        js = ('/static/admin/js/hide_attribute.js',)
 
        

admin.site.register(ProductStatus)
admin.site.register(ProductCategory)
admin.site.register(ProductSubCategory)
admin.site.register(ArrivalReason)
admin.site.register(DepartureReason)
admin.site.register(ProductIdentification, ProductIdentificationAdmin)
admin.site.register(InventoryCard, InventoryCardAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(ProductEnrty, ProductEntryAdmin)
admin.site.register(ProductOutlet, ProductOutletAdmin)
#admin.site.register(Permission)