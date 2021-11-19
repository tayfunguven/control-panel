from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput, Textarea
from Document.models import DemoDeliveryForm, DeviceDeliveryForm, RMAForm
from django.http import HttpResponseRedirect

class DemoDeliveryFormAdmin(admin.ModelAdmin):
    list_display = (
        'demo_id',
        'reference_number',
        'log_date',
        'delivery_address',
        'demo_duration',
        'client_company',
        'client_person',
    )

    search_fields = (
        'demo_id',
        'reference_number',
        'delivery_address',
        'client_company',
        'client_person',
    )

    date_hierarchy = 'log_date'
    filter_horizontal = ('product_id',)
    raw_id_fields = ('client_company', 'client_person')

    fieldsets = (
        (None, {
            "fields": (
                ('reference_number', 'log_date'),
                'delivery_address',
                'demo_duration',
                ('client_company','client_person'),
                'product_id'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':5, 'cols':100})},
        models.CharField: {'widget' : TextInput (attrs={'size':50})},
        #models.ManyToManyField: {'widget' : Textarea(attrs={'rows':5, 'cols':50})}
    }

    change_form_template = 'admin/print_change_list.html'
    def response_change(self, request, obj):
        if "_customaction" in request.POST:
            
            return HttpResponseRedirect('/print')
        else:
            return super(DemoDeliveryFormAdmin, self).response_change(request, obj)
    
class DeviceDeliveryFormAdmin(admin.ModelAdmin):
    list_display = (
        'device_delivery_id',
        'reference_number',
        'log_date',
        'delivery_address',
        'return_date',
        'client_company',
        'client_person',
    )

    search_fields = (
        'device_delivery_id',
        'reference_number',
        'delivery_address',
        'client_company',
        'client_person',
    )

    date_hierarchy = 'log_date'
    filter_horizontal = ('product_id',)
    raw_id_fields = ('client_company', 'client_person')

    fieldsets = (
        (None, {
            "fields": (
                ('reference_number', 'log_date'),
                'delivery_address',
                'return_date',
                ('client_company','client_person'),
                'product_id'
            ),
        }),
    )
    
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':5, 'cols':100})},
        models.CharField: {'widget' : TextInput (attrs={'size':50})},
        #models.ManyToManyField: {'widget' : Textarea(attrs={'rows':5, 'cols':50})}
    }

    change_form_template = 'admin/change_list.html'
    def response_change(self, request, obj):
        if "_customaction" in request.POST:
            
            return HttpResponseRedirect('/print')
        else:
            return super(DeviceDeliveryFormAdmin, self).response_change(request, obj)

class RMAFormAdmin(admin.ModelAdmin):
    list_display = (
        'rma_form_id',
        'rma_number',
        'log_date',
        'client_company',
        'client_person',
        'entry',
        'entry_description',
        'entry_analysis',
        'entry_note',
        'outlet',
        'rma_description'
    )

    date_hierarchy = 'log_date'
    raw_id_fields = (
        'client_company',
        'client_person',
        'entry',
        'outlet'
    )

    '''fieldsets = (
        (None, {
            "fields": (
                'rma_number', 'log_date',
            ),
        }),
        ('Müsteri Bilgileri', {
            "fields": (
                ('client_company', 'client_person'),
            ),
        }),
        ('Ürün Bilgileri', {
            "fields": (
                'entry',
            ),
        }),
        ('Ürün Girisi', {
            "fields": (
                'entry_description', ('entry_analysis', 'other_checked'), 'entry_note'
            ),
        }),
        ('Ürün Cikisi', {
            "fields": (
                'outlet', 'rma_description'
            ),
        }),
    )'''
    
    search_fields = (
        'rma_form_id',
        'rma_number',
        'client_company',
        'client_person',
        'entry',
        'entry_description',
        'entry_note',
        'outlet',
        'rma_description',
    )

admin.site.register(DemoDeliveryForm, DemoDeliveryFormAdmin)
admin.site.register(DeviceDeliveryForm, DeviceDeliveryFormAdmin)
admin.site.register(RMAForm, RMAFormAdmin)
