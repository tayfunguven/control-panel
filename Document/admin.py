from django.contrib import admin
from django.db import models
from django.forms.widgets import TextInput, Textarea
from Document.models import DemoDeliveryForm, DeviceDeliveryForm

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

admin.site.register(DemoDeliveryForm, DemoDeliveryFormAdmin)
admin.site.register(DeviceDeliveryForm, DeviceDeliveryFormAdmin)
