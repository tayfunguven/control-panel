from django.contrib import admin
from tinymce.widgets import TinyMCE
from django.db import models
from .models import ProductRegistration, ProductIdentifications, ProductOutlet, ProductEnrty
from import_export.admin import ImportExportModelAdmin
from Tracking.resources import ProductRegistrationResource
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, Spacer, TableStyle, Image, Paragraph
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
import os.path
import time
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER, TA_LEFT

styles = getSampleStyleSheet()

class ProductIdentificationsAdmin(admin.StackedInline):
    model = ProductIdentifications

#SUBCLASS OF MODEL OF ADMIN
class ProductRegistrationAdmin(ImportExportModelAdmin):
    def export_as_pdf(self, request, queryset):
        file_name = " ÜrünKayitlari-{0}.pdf".format(time.strftime("%d %B, %Y"))
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(file_name)
        title = "Ürün Kayıtları"
        #PDF DATA TABLE ROW NAMES
        data = [['Ürün Kodu', 'Ürün Adi', 'Ürün Adeti','Dahili No', 'Seri No', 'Ürün Durumu', 'Ürün Kategorisi',]]

        #ADD IMAGE FROM OS DIRECTORY
        fn = os.path.join(os.path.dirname(os.path.abspath(__file__)),'logo-momentomedya.png')
        img_data = Image(fn, 130, 50)
        #GET DATA WITH QUERY FROM MODEL
        for d in queryset.all():
            item = [d.product_id, d.product_name, d.product_amount, d.internal_number, d.serial_number, d.product_status, d.product_category]
            data.append(item)

        doc = SimpleDocTemplate(response, pagesize=A4)
        elements = []

        table_data = Table(data)
        table_data.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                                        ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                                        ("FONTSIZE",  (0, 0), (-1, -1), 8)]))
        textStyle = ParagraphStyle(
            name='Normal',
            parent=styles['Normal'],
            fontName='Helvetica',
            wordWrap='LTR',
            alignment=TA_LEFT,
            fontSize=12,
            leading=13,
            textColor=colors.black,
            borderPadding=0,
            leftIndent=0,
            rightIndent=0,
            spaceAfter=40,
            spaceBefore=0,
            splitLongWords=True,
            spaceShrinkage=0.05,
        )
        footerStyle = ParagraphStyle(
            name='Normal_CENTER',
            parent=styles['Normal'],
            fontName='Helvetica',
            wordWrap='LTR',
            alignment=TA_CENTER,
            fontSize=8,
            leading=13,
            textColor=colors.black,
            borderPadding=0,
            leftIndent=0,
            rightIndent=0,
            spaceAfter=0,
            spaceBefore=0,
            splitLongWords=True,
            spaceShrinkage=0.05,
        )

        #elements.append(img_data),
        #elements.append(Spacer(1, inch * 0.3))
        #elements.append(Paragraph("Stokta kayitli olan cihazlarin listesi asagida tablo olarak verilmistir.", textStyle))
        elements.append(table_data)
        #elements.append(Spacer(1, inch * 5.7))
        #elements.append(Paragraph("Halil Rifat Pasa Mah, Ilhanli Sk. No:14 D:2 Sisli/Istanbul", footerStyle))
        #elements.append(Paragraph("+90 212 222 80 50", footerStyle))
        #elements.append(Paragraph("www.momentomedya.com", footerStyle))
        doc.build(elements)
        return response


    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()}
    # }
    list_display = (
        'product_id',
        'product_name',
        'serial_number', 
        'internal_number', 
        'product_status',
        'product_category',
        'tested_status',
        'product_amount',
        'description',
        'photo',
        'additional_serials',
    )
    fieldsets = (
        ('Ürün Kayıt Bilgileri',
            {
                'fields' : ('product_id', 'product_name', 'has_serial', 'serial_number', 'internal_number', 
                            'product_status', 'product_category', 'tested_status',
                            'product_amount', 'description', 'photo',)
            }
        ),
    )
    list_filter = ('product_category','product_status',)
    search_fields = ('product_id', 'serial_number', 'internal_number','product_name','description','product_status','product_category','children__additional_serial')
    list_per_page = 15
    resource_class = ProductRegistrationResource
    actions = [export_as_pdf]
    export_as_pdf.short_description = "PDF olarak kaydet"
    inlines = [ProductIdentificationsAdmin]
    def additional_serials(self, obj):
        return ", ".join([
            child.additional_serial for child in obj.children.all()
        ])
    
    additional_serials.short_description = "Ek Seriler"
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return True

class ProductEntryAdmin(admin.ModelAdmin):
    list_display = (
        'entry_id',
        'purchase_price',
        'quantity',
        'date_arrival',
        'date_interval',
        'reason_arrival',
        'product_fk',
        'company_name'
    )
    fieldsets = (
        ('Ürün Kayıt Bilgileri',
            {
                'fields' : ('purchase_price',
                            'quantity',
                            'date_interval',
                            'reason_arrival',
                            'product_fk',
                            'company_name',)
            }
        ),
        ('Teslimat Bilgileri',
            {
                'fields' : ('deliverer_name',
                            'deliverer_surname',
                            'deliverer_company',
                            'deliverer_email',
                            'deliverer_phone',)
            }
        )
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return True
    

class ProductOutletAdmin(admin.ModelAdmin):
    list_display = (
        'outlet_id',
        'selling_price',
        'quantity',
        'date_departure',
        'date_interval',
        'reason_departure',
        'product_fk',
        'company_name'
    )

    fieldsets = (
        ('Ürün Kayıt Bilgileri',
            {
                'fields' : ('selling_price',
                            'quantity',
                            'date_interval',
                            'reason_departure',
                            'product_fk',
                            'company_name')
            }
        ),
        ('Teslimat Bilgileri',
            {
                'fields' : ('deliverer_name',
                            'deliverer_surname',
                            'deliverer_company',
                            'deliverer_email',
                            'deliverer_phone',)
            }
        )
    )
    def has_add_permission(self, request, obj=None):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(ProductRegistration,ProductRegistrationAdmin)
#admin.site.register(ProductEnrty, ProductEntryAdmin)
#admin.site.register(ProductOutlet, ProductOutletAdmin)


from django.contrib import admin
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        if (request.user.is_superuser):
            return True
        return False

    def has_view_permission(self, request, obj=None):
        #return request.user.is_superuser
        return True
    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"