from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
from .models import DemoDeliveryForm

from django.contrib.auth.decorators import login_required

@login_required
def render_pdf_view(request):
    template_path = 'Forms/demo_form.html'
    context = {
        'document_infos': DemoDeliveryForm.objects.all(),
    }
    print(DemoDeliveryForm.objects.all())
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # TO DOWNLOAD:
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    # TO DISPLAY:
    #response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
