from django.contrib import admin
from django.forms.widgets import Input
from import_export.admin import ExportMixin
from Finance.resources import *
from .models import *
from django.forms import TextInput
from django.db.models import Sum, Count, Avg, Q
from .models import PersonalIncomeSummary
from forex_python.converter import CurrencyRates
import datetime

###### COMPANY EXPENSE CLASSES ######
class CompanyExpenseInline(admin.TabularInline):
    model = CompanyExpense
    min_num = 1
    extra = 10
    #readonly_fields = ['log_date', 'expense_code', 'price', 'subtotal', 'vat_amount', 'grand_total']
    formfield_overrides = {
        models.CharField: {'widget' : TextInput (attrs={
            'size': 15
        
        })},
        models.DecimalField: {'widget' : Input (attrs={'size': 10})}
    }
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['log_date', 'expense_code', 'price', 'subtotal','vat_amount', 'grand_total', ]
        else:
            return ['log_date', 'expense_code', 'price', 'subtotal','vat_amount', 'grand_total', 'user']
 
class CompanyExpenseAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CompanyExpenseResource
    list_display = (
        'expense_code',
        'expense_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'price',
        'subtotal',
        'vat_rate',
        'vat_amount',
        'grand_total',
        'payment_type',
        'log_date',
        'expense_to'
    )
    readonly_fields = ['price', 'subtotal','vat_amount', 'grand_total', 'log_date']
    list_filter = ('expense_name', 'currency_type', 'log_date', 'payment_type')
    search_fields = ('expense_name', 'expense_code','expense_to')
    date_hierarchy = 'log_date'
    list_editable = (
        'expense_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'vat_rate',
        'payment_type',
        'expense_to'
    )

    def get_queryset(self, request):
        qs = super(CompanyExpenseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # print(SalaryInfo.objects.get('user'))
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class CompanyExpenseTableAdmin(admin.ModelAdmin):
    inlines = [CompanyExpenseInline]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False

###### PERSONAL EXPENSE CLASSES ######
class PersonalExpenseInline(admin.TabularInline):
    model = PersonalExpense
    min_num = 1
    extra = 10
    #readonly_fields = ['log_date', 'expense_code', 'price', 'subtotal', 'vat_amount', 'grand_total']
    formfield_overrides = {
        models.CharField: {'widget' : TextInput (attrs={
            'size': 15
        
        })},
        models.DecimalField: {'widget' : Input (attrs={'size': 10})}
    }
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['log_date', 'expense_code', 'price', 'subtotal','vat_amount', 'grand_total']
        else:
            return ['log_date', 'user', 'expense_code', 'price', 'subtotal','vat_amount', 'grand_total']
 
class PersonalExpenseAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = PersonalExpenseResource
    list_display = (
        'expense_code',
        'expense_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'price',
        'subtotal',
        'vat_rate',
        'vat_amount',
        'grand_total',
        'log_date',
        'user'
    )
    readonly_fields = ['price', 'subtotal','vat_amount', 'grand_total', 'log_date', 'expense_code']
    list_filter = ('expense_name', 'currency_type', 'log_date')
    search_fields = ('expense_name', 'expense_code')
    date_hierarchy = 'log_date'
    # list_editable = (
    #     'expense_name',
    #     'amount',
    #     'unit_id',
    #     'currency_price',
    #     'currency_type',
    #     'vat_rate',
    # )

    def get_queryset(self, request):
        qs = super(PersonalExpenseAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # print(SalaryInfo.objects.get('user'))
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class PersonalExpenseTableAdmin(admin.ModelAdmin):
    inlines = [PersonalExpenseInline]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False

class PersonalExpenseForUserEntryAdmin(admin.ModelAdmin):
    list_display = (
        'expense_code',
        'expense_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'price',
        'subtotal',
        'vat_rate',
        'vat_amount',
        'grand_total',
        'log_date',
        'user',
        'approval_status',
        'payment_status'
    )
    readonly_fields = ['log_date', 'expense_code', 'price', 'user','subtotal','vat_amount', 'grand_total', ]
    list_filter = ('currency_type', 'log_date', 'approval_status', 'payment_status')
    search_fields = ('expense_name', 'expense_code')
    date_hierarchy = 'log_date'
    
    # list_editable = (
    #     'expense_name',
    #     'amount',
    #     'unit_id',
    #     'currency_price',
    #     'currency_type',
    #     'vat_rate',
    # )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return [
                'expense_id', 'expense_code', 'expense_name',
                'amount', 'unit_id', 'currency_price', 'currency_type',
                'price', 'subtotal', 'vat_rate', 'vat_amount',
                'grand_total', 'user', 'log_date',
                ]
                    
        else:
            return ['expense_code', 'user', 'log_date', 'expense_code', 'price', 'subtotal','vat_amount', 'grand_total','approval_status','payment_status']
    
    def get_queryset(self, request):
        qs = super(PersonalExpenseForUserEntryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.get_full_name())

    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            obj.user = request.user.get_full_name()
            return obj.user, obj.save()
        else:
            return obj.save() 

    def has_change_permisson(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return False
        return True

###### Company INCOME CLASSES ######
class CompanyIncomeInline(admin.TabularInline):
    model = CompanyIncome
    min_num = 1
    extra = 10
    readonly_fields = ['log_date', 'income_code', 'price', 'subtotal', 'vat_amount', 'grand_total']
    formfield_overrides = {
        models.CharField: {'widget' : TextInput (attrs={
            'size': 15     
        })},
        models.DecimalField: {'widget' : Input (attrs={'size': 10})}
    }
      
class CompanyIncomeAdmin(ExportMixin, admin.ModelAdmin):
    resource_class = CompanyIncomeResource
    list_display = (
        'income_code',
        'income_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'price',
        'subtotal',
        'vat_rate',
        'vat_amount',
        'grand_total',
        'payment_type',
        'log_date',
        'income_to'
    )
    
    list_filter = ('income_name', 'currency_type', 'log_date', 'payment_type')
    search_fields = ('income_name','income_code','income_to')
    date_hierarchy = 'log_date'
    readonly_fields = ['log_date', 'grand_total', 'subtotal', 'vat_amount', 'grand_total']
    list_editable = (
        'income_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'vat_rate',
        'payment_type',
        'income_to'
    )

    def get_queryset(self, request):
        qs = super(CompanyIncomeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # print(SalaryInfo.objects.get('user'))
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class CompanyIncomeTableAdmin(admin.ModelAdmin):
    inlines = [CompanyIncomeInline]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False

###### PERSONAL INCOME CLASSES ######
class PersonalIncomeInline(admin.TabularInline):
    model = PersonalIncome
    min_num = 1
    extra = 10
    readonly_fields = ['log_date', 'income_code', 'price', 'subtotal', 'vat_amount', 'grand_total']
    formfield_overrides = {
        models.CharField: {'widget' : TextInput (attrs={
            'size': 15     
        })},
        models.DecimalField: {'widget' : Input (attrs={'size': 10})}
    }
      
class PersonalIncomeAdmin(ExportMixin, admin.ModelAdmin):
    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions
    resource_class = PersonalIncomeResource
    list_display = (
        'income_code',
        'income_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'price',
        'subtotal',
        'vat_rate',
        'vat_amount',
        'grand_total',
        'log_date',
        'user'
    )
    
    list_filter = ('income_name', 'currency_type', 'log_date')
    search_fields = ('income_name','income_code',)
    date_hierarchy = 'log_date'
    readonly_fields = ['log_date', 'grand_total', 'subtotal', 'vat_amount', 'grand_total']
    list_editable = (
        'income_name',
        'amount',
        'unit_id',
        'currency_price',
        'currency_type',
        'vat_rate',
    )

    def get_queryset(self, request):
        qs = super(PersonalIncomeAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    # print(SalaryInfo.objects.get('user'))
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class PersonalIncomeTableAdmin(admin.ModelAdmin):
    inlines = [PersonalIncomeInline]
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return False

class UnitNameAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return False

class ComissionAdmin(admin.ModelAdmin):
    list_display = (
        'comission_code',
        'type_id',
        'sales_price',
        'comission_rate',
        'total',
        'log_date',
        #'relateds',

    )
    list_filter = ('log_date', 'user')
    search_fields = ('comission_type', 'comission_code')
    date_hierarchy = 'log_date'
    # inlines = [ComissionRelatedInline]
    readonly_fields = ['total', 'log_date']
    # def relateds(self, obj):
    #     return ", ".join([
    #         child.user for child in obj.comissions.all()
    #     ])
    
    # relateds.short_description = "Personeller"
    def get_queryset(self, request):
        qs = super(ComissionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permisson(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class PunishmentAdmin(admin.ModelAdmin):
    list_display = (
        'punishment_code',
        'punishment_topic',
        'punishment_amount',
        'punishment_explanation',
        'user',
        'log_date'
    )
    list_filter = ('log_date', 'user', )
    date_hierarchy = 'log_date'
    search_fields = ('punishment_topic', 'punishment_code')
    readonly_fields = ['log_date',]
    def get_queryset(self, request):
        qs = super(PunishmentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class IncentiveAdmin(admin.ModelAdmin):
    list_display = (
        'incentive_code',
        'incentive_name',
        'incentive_amount',
        'user',
        'log_date'
    )
    search_fields = ('incentive_name', 'incentive_code')
    date_hierarchy = 'log_date'
    list_filter = ('user','log_date',)
    readonly_fields = ['log_date',]
    
    def get_queryset(self, request):
        qs = super(IncentiveAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

class AdvancePaymentAdmin(admin.ModelAdmin):
    list_display = (
        'payment_code',
        'payment_amount',
        'user',
        'description',
        'log_date'
    )
    readonly_fields = ['log_date',]
    list_filter = ['user',]
    date_hierarchy = 'log_date'

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def get_queryset(self, request):
        qs = super(AdvancePaymentAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return []
        else:
            return ['log_date','description']

class SalaryInfoAdmin(admin.ModelAdmin):
    list_display = (
        'salary_info_code',
        'salary',
        'user',
        'log_date'
    )
    date_hierarchy = 'log_date'
    search_fields = ('salary_info_code',)
    list_filter = ('user', 'log_date')
    readonly_fields = ['log_date',]

    def get_queryset(self, request):
        qs = super(SalaryInfoAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

@admin.register(PersonalIncomeSummary)
class PersonalIncomeSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/income_summary_change_list.html'
    date_hierarchy = 'log_date'
    
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'grand_tot': Sum('grand_total'),
        }
        # def daily_currency():
        #     c = CurrencyRates()
        #     result = c.get_rate('USD','TRY')
        #     return str(result)
        # res = daily_currency()
        response.context_data['summary'] = list(
            qs
            .values(
                'income_code',
                'income_name',
                'amount',
                'unit_id',
                'currency_price',
                'currency_type',
                'price',
                'subtotal',
                'vat_rate',
                'vat_amount',
                'grand_total',
                'log_date',
                'user'
            )
            .annotate(**metrics)
            .order_by('-log_date'),
        )
        
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics),           
        )
        return response
    
    list_filter = (
        'currency_type',
    )

    def get_queryset(self, request):
        qs = super(PersonalIncomeSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False
        
    def has_delete_permission(self, request, obj=None):
        return False
    
@admin.register(PersonalExpenseSummary)
class PersonalExpenseSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/expense_summary_change_list.html'
    date_hierarchy = 'log_date'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'grand_tot': Sum('grand_total'),
        }

        response.context_data['summary'] = list(
            qs
            .values(
                'expense_code',
                'expense_name',
                'amount',
                'unit_id',
                'currency_price',
                'currency_type',
                'price',
                'subtotal',
                'vat_rate',
                'vat_amount',
                'grand_total',
                'log_date',
                'user'
            )
            .annotate(**metrics)
            .order_by('-log_date')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response
    
    list_filter = (
        'currency_type',
    )

    def get_queryset(self, request):
        qs = super(PersonalExpenseSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        return False

    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(CompanyIncomeSummary)
class CompanyIncomeSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/company_income_summary_change_list.html'
    date_hierarchy = 'log_date'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'grand_tot': Sum('grand_total'),
        }

        response.context_data['summary'] = list(
            qs
            .values(
                'income_code',
                'income_name',
                'amount',
                'unit_id',
                'currency_price',
                'currency_type',
                'price',
                'subtotal',
                'vat_rate',
                'vat_amount',
                'grand_total',
                'payment_type',
                'log_date',
                'income_to'
            )
            .annotate(**metrics)
            .order_by('-log_date')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response
    
    list_filter = (
        'currency_type',
    )

    def get_queryset(self, request):
        qs = super(CompanyIncomeSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    
@admin.register(CompanyExpenseSummary)
class CompanyExpenseSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/company_expense_summary_change_list.html'
    date_hierarchy = 'log_date'
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'grand_tot': Sum('grand_total'),
        }

        response.context_data['summary'] = list(
            qs
            .values(
                'expense_code',
                'expense_name',
                'amount',
                'unit_id',
                'currency_price',
                'currency_type',
                'price',
                'subtotal',
                'vat_rate',
                'vat_amount',
                'grand_total',
                'payment_type',
                'log_date',
                'expense_to'
            )
            .annotate(**metrics)
            .order_by('-log_date')
        )
        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )
        return response
    
    list_filter = (
        'currency_type',
    )

    def get_queryset(self, request):
        qs = super(CompanyExpenseSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def has_add_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(CompanyExpenseTable, CompanyExpenseTableAdmin)
admin.site.register(CompanyIncomeTable, CompanyIncomeTableAdmin)
admin.site.register(CompanyExpense,CompanyExpenseAdmin)
admin.site.register(CompanyIncome, CompanyIncomeAdmin)
admin.site.register(PersonalExpenseTable, PersonalExpenseTableAdmin)
admin.site.register(PersonalIncomeTable, PersonalIncomeTableAdmin)
admin.site.register(PersonalExpense, PersonalExpenseAdmin)
admin.site.register(PersonalIncome, PersonalIncomeAdmin)
admin.site.register(AdvancePayment, AdvancePaymentAdmin)
admin.site.register(SalaryInfo, SalaryInfoAdmin)
admin.site.register(Punishment, PunishmentAdmin)
admin.site.register(Comission, ComissionAdmin)
admin.site.register(Incentive, IncentiveAdmin)
admin.site.register(UnitName, UnitNameAdmin)
admin.site.register(PersonalExpenseForUserEntry, PersonalExpenseForUserEntryAdmin)
