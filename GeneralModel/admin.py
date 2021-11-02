from django.contrib import admin
from GeneralModel.models import Firm, FirmAuthorizedPerson, DeliveryCompany

class FirmAdmin(admin.ModelAdmin):
    list_display = (
        'firm_id',
        'company_name',
        'business_field',
        'e_mail',
        'phone',
        'address',
        'tax_administration',
        'tax_number',
        'mersis_number',
        'company_title',
        'official_address'
    )

    list_display_links = (
        'company_name',
        'business_field',
        'e_mail',
        'phone',
        'address',
        'tax_administration',
        'tax_number',
        'mersis_number',
        'company_title',
        'official_address'
    )
    
    fieldsets = (
        ('Firma Bilgisi', {'fields':(('company_name', 'business_field'), ('phone', 'e_mail'), 'address')}

        ),
        ('Fatura Bilgisi', {
            'fields': ('has_invoice','tax_administration', ('tax_number', 'mersis_number'), 'company_title', 'official_address')
        }),
    )
    search_fields = ('company_name', 'e_mail', 'phone', 'address', 'tax_administration', 'tax_number', 'mersis_number', 'company_title', 'official_address')
    
class FirmAuthorizedPersonAdmin(admin.ModelAdmin):
    list_display = (
        'person_id',
        'first_name',
        'last_name',
        'company',
        'authorized_title',
        'phone',
        'e_mail',
    )

    list_display_links = (
        'first_name',
        'last_name',
        'company',
        'authorized_title',
        'phone',
        'e_mail',
    )


admin.site.register(Firm, FirmAdmin)
admin.site.register(FirmAuthorizedPerson, FirmAuthorizedPersonAdmin)
admin.site.register(DeliveryCompany,)