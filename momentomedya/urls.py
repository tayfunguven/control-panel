from django.urls import path
from django.conf.urls import url
from momentomedya.models import RMAApply
from . import views

app_name = "momentomedya"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact", views.contactpage, name="contactpage"),
    path("references", views.referencespage, name="referencespage"),
    path('RMAForm', views.RmaForm, name='RMAForm'),
    ]


