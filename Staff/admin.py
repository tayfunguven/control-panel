from django.contrib import admin
from django.db import models
from Staff.models import *
from import_export.admin import ImportExportModelAdmin
from django.forms import TextInput, Textarea
from nested_inline.admin import NestedModelAdmin, NestedStackedInline

class EmployeeAdmin(admin.ModelAdmin):
    list_filter = ('employee_name',)
    search_fields = ('employee_name', 'employee_id', 'employee_surname')
    list_per_page = 10
    list_display = (
        'employee_id',
        'employee_name',
        'employee_surname',
        'employee_phone',
        'employee_email',
    )
    fieldsets = (
        ('Bilgiler',
            {
                'fields' : ('employee_name', 'employee_surname')
            }
        ),
        ('İletişim',
            {
                'fields' : ('employee_phone', 'employee_email')
            }
        )
    )

    def has_add_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
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

class PermitRequestAdmin(ImportExportModelAdmin):
    list_per_page = 10
    list_filter = ('user', 'approval_status','permit_choice','permit_type')
    search_fields = ('user', 'permit_reason','permit_choice','permit_type')
    list_display = (
        'user',
        'approval_status',
        'permit_type',
        'permit_reason',
        'date_start',
        'date_end',
        'permit_choice',
        'permit_document',
        'permit_id',
    )
    fieldsets = (
        ('Personel Bilgileri',
            {
                'fields' : ('user', 'approval_status')
            }
        ),
        ('Talep Bilgileri',
            {
                'fields' : ('date_start', 'date_end', 'permit_choice', 'permit_type', 'permit_reason', 'permit_document')
            }
        )
    )
    #CRUD OPERATIONS
    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    #function that gets query set for user that only can view his/her own entry
    def get_queryset(self, request):
        qs = super(PermitRequestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.get_full_name())
    #function that prevent user name changes if superuser tries to change something
    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            obj.user = request.user.get_full_name()
            return obj.user, obj.save()
        else:
            return obj.save()    



        # if request.user.is_superuser:
        #     if obj.pk is None: #cheks that if objects primary key is null -> #add else -> #change
        #         obj.user = request.user
        #         obj.save()
        #     obj.save()
        # if obj.pk is None:
        #     obj.user = request.user
        #     obj.save()
        # obj.save()
    #makes some fields readonly for only superuser can change
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['user',]
        else:
            if obj is None:
                return ['approval_status','user',]
            field_value = getattr(obj, 'approval_status')
            print(field_value)
            if field_value=="Onaylandi" or field_value == "Reddedildi":
                return ['date_start', 'date_end', 'permit_choice', 'permit_type', 'permit_reason', 'approval_status','user', 'permit_document' ]
            return ['approval_status','user',]   

class AdvanceRequestAdmin(ImportExportModelAdmin):
    list_filter = ('user', 'request_date')
    search_fields = ('user', 'approval_status','advance_reason')
    list_per_page = 10
    list_display = (
        'user',
        'advance_amount',
        'approval_status',
        'request_date',
        'short_description',
        'advance_id',
    )
   
    fieldsets = (
        ('Personel Bilgileri',
            {
                'fields' : ('user', 'approval_status')
            }
        ),
        ('Talep Bilgileri',
            {
                'fields' : ('request_date', 'advance_amount','advance_reason')
            }
        )
    )

    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':10, 'cols':20})},

    }

    #CRUD OPERATIONS
    def has_add_permission(self, request, obj=None):
        return True
    
    def has_view_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    #function that gets query set for user that only can view his/her own entry
    def get_queryset(self, request):
        qs = super(AdvanceRequestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.get_full_name())

    #function that prevent user name changes if superuser tries to change something    
    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            obj.user = request.user.get_full_name()
            return obj.user, obj.save()
        else:
            return obj.save() 

    #makes some fields readonly for only superuser can change
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['user',]
        else:
            if obj is None:
                return ['approval_status','user',]
            field_value = getattr(obj, 'approval_status')
            print(field_value)
            if field_value=="Onaylandi" or field_value == "Reddedildi":
                return ['advance_amount', 'request_date', 'advance_reason','approval_status','user' ]
            return ['approval_status','user',]

class ReportContentInline(NestedStackedInline):
    model = ReportContent
    min_num = 1
    max_num = 20
    extra = 0
    fk_name = 'report_id'
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':5, 'cols':100})},
        models.CharField: {'widget' : TextInput (attrs={'size':50})},
        #models.ManyToManyField: {'widget' : Textarea(attrs={'rows':5, 'cols':50})}
    }
    fieldsets = (
        ('Rapor İçeriği', {'fields':('title', 'job_type', 'job_status','work_progress','description','report_document',)}

        ),
        ('Momento Medya İlgililer', {
            'classes': ('collapse',),
            'fields': ('related_person',)
        }),
        ('Firmalar', {
            'classes': ('collapse',),
            'fields': ('company', 'company_authorized'),
        }),
    )
    filter_horizontal = ('company', 'company_authorized', 'related_person',)

    class Media:
        css = {
            'all': ('admin/css/resize-widget.css',), # if you have saved this file in `static/css/` then the path must look like `('css/resize-widget.css',)`
        }

    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
class ReportAdmin(NestedModelAdmin):
    list_per_page = 10
    list_filter = ('report_date', 'user',)
    date_hierarchy = 'report_date'
    search_fields = ('user',)
    list_display = (
        'user',
        'report_date',
        'report_title',
        'report_job_type',
        'report_job_status',
        'report_work_progress',
        'report_related_person',
        'report_company',
        'report_company_authorized',
            
    )
    list_display_links = (
        'user',
        'report_date',
        'report_title',
        'report_job_type',
        'report_job_status',
        'report_work_progress',
        'report_related_person',
        'report_company',
        'report_company_authorized',
            
    )
    inlines = [ReportContentInline]
    def report_title(self, obj):
        return ", ".join(
            [child.title for child in obj.reports.all()]
        )
    
    def report_job_type(self, obj):
        return ", ".join(
            [str(child.job_type) for child in obj.reports.all()]
        )
    
    def report_job_status(self, obj):
        return ", ".join(
            [child.job_status for child in obj.reports.all()]
        )

    def report_work_progress(self, obj):
        return ", ".join(
            [child.work_progress for child in obj.reports.all()]
        )
    
    def report_related_person(self, obj):
        return ", ".join(
            [str(child.related_person.all()) for child in obj.reports.all()]
        )
    
    def report_company(self, obj):
        return ", ".join(
            [str(child.company.all()) for child in obj.reports.all()]
        )
    
    def report_company_authorized(self, obj):
        return ", ".join(
            [str(child.company_authorized.all()) for child in obj.reports.all()]
        )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            'report_related_person',
            'report_company',
            'report_company_authorized',
        )

    report_title.short_description = "Başlık"
    report_job_type.short_description = "İş Türü"
    report_job_status.short_description = "İş Statüsü"
    report_work_progress.short_description = "İş Durumu"
    report_related_person.short_description = "Momento Medya İlgili/İlgililer"
    report_company.short_description = "Firma/Firmalar"
    report_company_authorized.short_description = "Firma İlgilisi/İlgilileri"

    #CRUD OPERATIONS
    def has_add_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False
        
    #function that gets query set for user that only can view his/her own entry
    def get_queryset(self, request):
        qs = super(ReportAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user.get_full_name())
    #function that prevent user name changes if superuser tries to change something
    def save_model(self, request, obj, form, change):
        if obj.pk is None: #cheks the object has been created before or not
            obj.user = request.user.get_full_name()
            return obj.user, obj.save()
        else:
            return obj.save()   

    #makes some fields readonly for only superuser can change
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['user',]
        else:
            return ['report_date', 'user',]

class AuthorizedPersonAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job_title',
        'phone',
        'e_mail',
    )

    list_display_links = (
        'first_name',
        'last_name',
        'job_title',
        'phone',
        'e_mail',
    )
    def has_add_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(PermitRequest,PermitRequestAdmin)
admin.site.register(AdvanceRequest, AdvanceRequestAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(JobType)
admin.site.register(AuthorizedPerson, AuthorizedPersonAdmin)

class BusinessTaskCommentInline(admin.StackedInline):
    model = BusinessTaskComment
    extra = 1
    fieldsets = (
        (None, {
            "fields": (
                'comment', 'attach', 'tag_person'
            ),
        }),
    )
    formfield_overrides = {
        models.TextField: {'widget' : Textarea (attrs={'rows':5, 'cols':100})},
        #models.CharField: {'widget' : TextInput (attrs={'size':50})},
        #models.ManyToManyField: {'widget' : Textarea(attrs={'rows':5, 'cols':50})}
    }
    
    def has_add_permission(self, request, obj=None):
        return True
    
    def has_change_permission(self, request, obj=None):
        return False

class BusinessTaskAdmin(admin.ModelAdmin):
    inlines = [BusinessTaskCommentInline]
    list_display = (
        'title',
        'created_at',
        'deadline',
        'state',
        'priority',
    )
    list_display_links = (
        'title',
        'created_at',
        'deadline',
        'state',
        'priority',
    )
    search_fields = (
        'title',
        'attach',
    )
    list_filter = (
        'state',
        'priority',
    )
    fieldsets = (
        ('Task', {
            'fields': ('title', 'assigned_to', ('created_at', 'deadline'),('state', 'priority'),'description', 'attach'),
        }),
    )
    def save_formset(self, request, form, formset, change):
        if formset.model != BusinessTaskComment:
            return super(BusinessTaskAdmin, self).save_formset(request, form, formset, change)
        instances = formset.save(commit=False)
        for instance in instances:
            if not instance.pk:
                instance.author = request.user.get_full_name()
            instance.save()
        formset.save_m2m()
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser and request.user.has_perm('Staff.task_edit_field_permission'):
            return []
        else:
            return ['title', 'assigned_to', 'created_at', 'deadline', 'state', 'priority', 'description', 'attach']
            
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "assigned_to":
            kwargs["queryset"] = User.objects.filter(groups='5')
        return super(BusinessTaskAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)
    
    def get_queryset(self, request):
        qs = super(BusinessTaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(assigned_to=request.user)

admin.site.register(BusinessTask, BusinessTaskAdmin)    