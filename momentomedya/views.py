from django.shortcuts import render
from django.http import HttpResponse


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