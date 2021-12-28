from django.contrib.admin.models import ADDITION, LogEntry
from django.http import response
from ProjectForm.models import Dealer, DealerProjectSummary, DealerUser, InventoryForDealer, RegisterDeal, RegisterLogs
from django.contrib import admin

class RegisterDealAdmin(admin.ModelAdmin):
    search_fields = (
        'project_name',
        'user',
        'project_description',
        'company',
        'company_address',
        'contact_name',
        'contact_surname',
        'contact_email',
        'contact_phone'
    )
    list_filter = (
        'user',
        'company',
        'project_status',
    )
    list_display = (
        'project_name',
        'company',
        'project_date',
        'project_time',
        'project_status',
        'user',
    )
    list_display_links = (
        'project_name',
        'company',
        'project_date',
        'project_time',
        'project_status',
        'user',
    )
    fieldsets = (
        ('Proje Bilgileri',
            {
                'fields' : ('is_displayed',('project_name', 'project_subject',),( 'project_date','estimated_date', 'project_time'), 'user', 'project_status', 'project_description')
            }
        ),
        ('Kurum Bilgileri',
            {
                'fields' : ('company', 'company_address', )
            }
        ),
        ('Kurum Yetkili Bilgileri',
            {
                'fields' : (('contact_name', 'contact_surname'), ('contact_phone', 'contact_email'))
            }
        )
    )


    def get_queryset(self, request):
        qs = super(RegisterDealAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.username =='aviwest':
            return qs
        #return qs.filter(user=request.user.get_full_name())
        return qs.filter(user=request.user)
    #function that prevent user name changes if superuser tries to change something
    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            #obj.user = request.user.get_full_name()
            obj.user = request.user
            return obj.user, obj.save()
        else:
            return obj.save()   

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['user', 'project_date','project_time',]
        else:
            if obj is None:
                return ['user', 'project_date','project_time',]
            return ['is_displayed', 'user', 'project_date', 'project_time', 'company', 'company_address', 'estimated_date']   

class RegisterLogAdmin(admin.ModelAdmin):
    search_fields = (
        'project_name',
        'user',
        'project_description',
        'manager_note',
        'company',
        'company_address',
        'contact_name',
        'contact_surname',
        'contact_email',
        'contact_phone'
    )
    list_filter = (
        'user',
        'approval',
        'company',
        'project_status',
    )
    list_display = (
        'project_name',
        'approval',
        'project_status',
        'company',
        'user',
        'project_time',
        'project_date',
    )
    list_display_links = (
        'project_name',
        'company',
        'project_date',
        'project_time',
        'project_status',
        'user',
    )
    fieldsets = (
        ('Proje Bilgileri',
            {
                'fields' : ('is_displayed', 'project_name', 'project_subject', 'project_date','estimated_date', 'project_time', 'approval', 'manager_note', 'user', 'project_status', 'project_description')
            }
        ),
        ('Kurum Bilgileri',
            {
                'classes': ('collapse',),
                'fields' : ('company', 'company_address', )
            }
        ),
        ('Kurum Yetkili Bilgileri',
            {
                'classes': ('collapse',),
                'fields' : ('contact_name', 'contact_surname', 'contact_phone', 'contact_email')
            }
        )
    )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return [
                'project_name',
                'project_subject',
                'project_date',
                'estimated_date',
                'project_time',
                'user',
                'project_status',
                'project_description',
                'company',
                'company_address',
                'contact_name',
                'contact_surname',
                'contact_phone',
                'contact_email',
            ]
        else:
            return [
                'project_name',
                'project_subject',
                'approval',
                'project_date',
                'estimated_date',
                'project_time',
                'manager_note',
                'user',
                'project_status',
                'project_description',
                'company',
                'company_address',
                'contact_name',
                'contact_surname',
                'contact_phone',
                'contact_email',
            ]

    def get_queryset(self, request):
        qs = super(RegisterLogAdmin, self).get_queryset(request)
        if request.user.is_superuser or request.user.username =='aviwest':
            return qs
        #return qs.filter(user=request.user.get_full_name())
        return qs.filter(user=request.user)
    #function that prevent user name changes if superuser tries to change something
    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            #obj.user = request.user.get_full_name()
            obj.user = request.user
            return obj.user, obj.save()
        else:
            return obj.save()   

    #def has_add_permission(self, request, obj=None):
    #    return False
    #def has_change_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False
    #def has_view_permission(self, request, obj=None):
    #    return True
    #def has_delete_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False

@admin.register(DealerProjectSummary)
class DealerProjectSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/dealer_project_summary_change_list.html'
    date_hierarchy = 'project_date'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        response.context_data['summary'] = list(
            qs
            .values(
                'project_name',
                'project_subject',
                'approval',
                'project_status',
                'user',
                'manager_note',
            )
            #.order_by('-log_date')
        )
        return response
    
    list_filter = (
        'approval',
    )
    search_fields = ('project_name', 'project_subject',
                'user',
                )
    
    def get_queryset(self, request):
        from django.db.models import Q
        qs = super(DealerProjectSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter(Q(approval ='onaylandi', is_displayed = True, project_name__contains='İLK KAYIT') | Q(approval ='bosta', is_displayed = True, project_name__contains='İLK KAYIT'))
        return qs.filter(Q(approval ='onaylandi', is_displayed = True, project_name__contains='İLK KAYIT') | Q(approval ='bosta', is_displayed = True ,project_name__contains='İLK KAYIT'))

    #def has_add_permission(self, request, obj=None):
    #    return False
    #def has_view_permission(self, request, obj=None):
    #    return True
    #def has_change_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False
    #def has_delete_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False


class InventoryForDealerAdmin(admin.ModelAdmin):
    change_list_template = 'admin/inventory_for_dealer.html'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        response.context_data['products'] = list(
            qs
            .values(
                'product_code',
                'product_name',
                'product_quantity',
                'recommended_price',
                'money_unit',
                'description'
            )
            #.order_by('-log_date')
        )
        return response
    
    search_fields = ('product_code',
                'product_name',
                'description')
    
    def get_queryset(self, request):
        qs = super(InventoryForDealerAdmin, self).get_queryset(request)
        return qs

    #def has_add_permission(self, request, obj=None):
    #    return False
    #def has_view_permission(self, request, obj=None):
    #    return True
    #def has_change_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False
    #def has_delete_permission(self, request, obj=None):
    #    if request.user.is_superuser:
    #        return True
    #    return False






admin.site.register(RegisterDeal, RegisterDealAdmin)
admin.site.register(RegisterLogs, RegisterLogAdmin)
# admin.site.register(Dealer)
# admin.site.register(DealerUser)
