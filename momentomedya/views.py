from django.db import models
from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, request
from .models import RMAApply
from django.contrib import messages 
from .forms import CareerForm, RMAForm

def homepage(request):
    return render(request = request,
                  template_name = "momentomedya/index.html",
                  context = {}
                 )

def contactpage(request):
    return render(request = request,
                  template_name = "momentomedya/contact.html",
                  context = {}
                 )

def referencespage(request):
    return render(request = request,
                  template_name = "momentomedya/references.html",
                  context = {}
                 )

# def careerpage(request):
#     return render(request = request,
#                   template_name = "momentomedya/career.html",
#                   context={}
#                  )

def careerpage (request):
    submitted = False
    if request.method == 'POST':
        form = CareerForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/careerform?submitted=True')
    else:
        form = CareerForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request = request,
                  template_name = "momentomedya/careerform.html",
                  context = {'form':form, 'submitted':submitted}
                  )


def RmaForm (request):
    submitted = False
    if request.method == 'POST':
        form = RMAForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/RMAForm?submitted=True')
    else:
        form = RMAForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request = request,
                  template_name = "momentomedya/RMAForm.html",
                  context = {'form':form, 'submitted':submitted}
                  )

# def rmabasvurupage(request):
#     if request.method == 'POST':
#         rmabasvurupage()
    
#         return render(request= request,
#                  template_name = "momentomedya/RmaBasvuru.html",
#                  context={}
#                  )

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # class Rmabasvurupage(models.Model):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def get(self, request):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         RMAApply.objects.all()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         return render (request= request,
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                         template_name="momentomedya/RmaBasvuru.html",
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                         context = {}             
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #                         )
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #     def post(self, request):
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         Saverecord = RMAApply()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #         if Saverecord.is_valid():
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_first_name = request.POST['customer_first_name']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_last_name = request.POST['customer_last_name']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_company = request.POST['customer_company']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_email = request.POST['customer_email']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_phone = request.POST['customer_phone']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.customer_address = request.POST['customer_address']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.product_brand = request.POST['product_brand']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.product_model = request.POST['product_model']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.product_serial = request.POST['product_serial']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.apply_topic = request.POST['apply_topic']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.problems = request.POST['problems']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.problem_note = request.POST['problem_note']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.pdpb_approval = request.POST['pdpb_approval']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.other_chechked = request.POST['other_chechked']
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #             Saverecord.save()


# # # # # # # # # # # def rmabasvurupage(request):
# # # # # # # # # # #     return render(request = request,
# # # # # # # # # # #                   template_name = "momentomedya/rmabasvuru.html",
# # # # # # # # # # #                   context = {}
# # # # # # # # # # #                  )
# # # # # # # # # # # # # # # # # # # # # def rmabasvuru(self, request):
# # # # # # # # # # # # # # # # # # # # #  if request.method == 'POST':
# # # # # # # # # # # # # # # # # # # # #      RMAApply.objects.all()
# # # # # # # # # # # # # # # # # # # # #      RMAApply.save()  
     
    # saverecor=RMAApply()
     
            # # # # customer_first_name = request.POST['customer_first_name']
            # # # # customer_last_name = request.POST['customer_last_name']
            # # # # customer_company = request.POST['customer_company']
            # # # # customer_email = request.POST['customer_email']
            # # # # customer_phone = request.POST['customer_phone']
            # # # # customer_address = request.POST['customer_address']
            # # # # product_brand = request.POST['product_brand']
            # # # # product_model = request.POST['product_model']
            # # # # product_serial = request.POST['product_serial']
            # # # # apply_topic = request.POST['apply_topic']
            # # # # problems = request.POST['problems']
            # # # # problem_note = request.POST['problem_note']
            # # # # pdpb_approval = request.POST['pdpb_approval']
            # # # # other_chechked = request.POST['other_chechked']
            # # # # objects.create(customer_first_name=customer_first_name, customer_last_name=customer_last_name, customer_company=customer_company, customer_address=customer_address, customer_email=customer_email, customer_phone=customer_phone, product_brand=product_brand, product_model=product_model, product_serial=product_serial, apply_topic=apply_topic, problems=problems, problem_note=problem_note, pdpb_approval=pdpb_approval, other_chechked=other_chechked)
    #  saverecor.save()
#      return render(request= request,
#                  template_name = "momentomedya/RmaBasvuru.html",
#                  context={}
#                  )
#  else:
#      return render(request= request,
#                  template_name = "momentomedya/RmaBasvuru.html",
#                  context={}
#                  )

# # def rmabasvurupage(request):
# #     if request.method == 'POST':
#         if  request.POST.get('apply_id') and request.POST.get('customer_first_name') and request.POST.get('customer_last_name') and request.POST.get('customer_company') and request.POST.get('customer_email') and request.POST.get('customer_phone') and request.POST.get('customer_address') and request.POST.get('product_brand') and request.POST.get('product_model') and request.POST.get('product_serial') and request.POST.get('apply_topic') and request.POST.get('problems') and request.POST.get('problem_note') and request.POST.get('pdpb_approval'):
#             RMAApply.save()
#             return render(request= request,
#                     template_name = "momentomedya/RmaBasvuru.html",
#                     context={}
#                     )
# # id = request.POST.get("customer_first_name")
# #         ln = request.POST.get("customer_last_name")
# #         cc = request.POST.get("customer_company")
# #         ce = request.POST.get("customer_email")
# #         cp = request.POST.get("customer_phone")
# #         ca = request.POST.get("customer_address")
# #         pb = request.POST.get("product_brand")
# #         pm = request.POST.get("product_model")
# #         ps = request.POST.get("product_serial")
# #         at = request.POST.get("apply_topic")
# #         p = request.POST.getlist("problems")
# #         pn = request.POST.get("problem_note")
# #         oc = request.POST.get("other_chechked")
# #         pa = request.POST.get("pdpb_approval")
# #         o_ref = RMAApply(customer_first_name = id, customer_last_name = ln, customer_company = cc, customer_email = ce, customer_phone = cp, customer_address = ca, product_brand = pb, product_model = pm, product_serial = ps, apply_topic = at, problems = p, problem_note = pn, other_chechked = oc, pdpb_approval = pa )
# # #o_ref= (id, ln, cc, ce, cp, ca, pb, pm, ps, at, p, pn, oc, pa)
# #         o_ref.save()
#     #o_ref = RMAApply(customer_first_name = id, customer_last_name = ln, customer_company = cc, customer_email = ce, customer_phone = cp, customer_address = ca, product_brand = pb, product_model = pm, product_serial = ps, apply_topic = at, problems = p, problem_note = pn, other_chechked = oc, pdpb_approval = pa )

    # # # # # # # # # # # # if request.method == 'POST':
    # # # # # # # # # # # #     if  request.POST.get('customer_first_name') and request.POST.get('customer_last_name') and request.POST.get('customer_company') and request.POST.get('customer_email') and request.POST.get('customer_phone') and request.POST.get('customer_address') and request.POST.get('product_brand') and request.POST.get('product_model') and request.POST.get('product_serial') and request.POST.get('apply_topic') and request.POST.get('problems') and request.POST.get('problem_note') and request.POST.get('pdpb_approval'): 
    # # # # # # # # # # # #         True,
    # # # # # # # # # # # #         RMAApply.objects.get_or_create(
    # # # # # # # # # # # #             customer_first_name=request.POST.get("customer_first_name"), 
    # # # # # # # # # # # #             customer_last_name=request.POST.get("customer_last_name"),
    # # # # # # # # # # # #             customer_company=request.POST.get("customer_company"),
    # # # # # # # # # # # #             customer_email =request.POST.get("customer_email"),
    # # # # # # # # # # # #             customer_phone =request.POST.get("customer_phone"),
    # # # # # # # # # # # #             customer_address =request.POST.get("customer_address"),
    # # # # # # # # # # # #             product_brand=request.POST.get("product_brand"),
    # # # # # # # # # # # #             product_model=request.POST.get("product_model"),
    # # # # # # # # # # # #             product_serial=request.POST.get("product_serial"),
    # # # # # # # # # # # #             apply_topic=request.POST.get("apply_topic"),
    # # # # # # # # # # # #             problems=request.POST.getlist("problems"),
    # # # # # # # # # # # #             problem_note=request.POST.get("problem_Note"),
    # # # # # # # # # # # #             other_chechked=request.POST.get("other_chechked"),
    # # # # # # # # # # # #             pdpb_approval=request.POST.get("pdpb_approval"),
    # # # # # # # # # # # #             )
    # # # # # # # # # # # #         RMAApply.save()
    # # # # # # # # # # # #         messages.success(request, 'Başarıyla Gönderildi!')
    # # # # # # # # # # # #         return render(request= request,
    # # # # # # # # # # # #                  template_name = "momentomedya/RmaBasvuru.html",
    # # # # # # # # # # # #                  context={}
    # # # # # # # # # # # #                  )
    # # # # # # # # # # # #     else:
    # # # # # # # # # # # #      messages.warning(request, 'Bilgileri eksik girdiniz!')
    # # # # # # # # # # # #      return render(request= request,
    # # # # # # # # # # # #      template_name = "momentomedya/RmaBasvuru.html",
    # # # # # # # # # # # #      context={}
    # # # # # # # # # # # #      )
    # # # # # # # # # # # # else :
    # # # # # # # # # # # #     messages.warning(request, 'Bilgileri eksik girdiniz!')
    # # # # # # # # # # # #     return render(request= request,
    # # # # # # # # # # # #      template_name = "momentomedya/RmaBasvuru.html",
    # # # # # # # # # # # #      context={}
    # # # # # # # # # # # #      )
        #  # else:
        #     return render(request= request,
        #               template_name = "momentomedya/RmaBasvuru.html",
        #               context={}
        #              )

# # # # # #  def new_func(request, Saverecord):
# # # # # #       if Saverecord.is_valid():
# # # # # #           Saverecord.save
# # # # # #       messages.success(request, 'Başarıyla Gönderildi!')

    #if request.method == "POST":
     #   request.POST.get(customer_first_name=request.POST['inputName'])
      #  request.POST.get(customer_last_name=request.POST['inputSurname'])
      #  request.POST.get(customer_company=request.POST['inputCompanyName'])
      #  request.POST.get(customer_email=request.POST['inputEposta'])
       # request.POST.get(customer_phone=request.POST['inputTel'])
        #request.POST.get(customer_address=request.POST['inputAdress'])
        #request.POST.get(product_brand=request.POST['inputBrand'])
        #request.POST.get(product_model=request.POST['inputModel'])
        #request.POST.get(product_serial=request.POST['inputSeriNo'])
        #request.POST.get(apply_topic=request.POST['inputAciklama'])
        #request.POST.get(problems=request.POST['RMA_CHOICES'])
        #request.POST.get(problem_not=request.POST['inputNote'])
        #request.POST.get(other_chechked=request.POST[''])
        #request.POST.get(pdpb_approval=request.POST['onaylama'])
        #if RMAApply.is_valid():
         #   return HttpResponseRedirect('/thanks')
        #else:
         #   return Http404

