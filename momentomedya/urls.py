from django.urls import path
from . import views

app_name = "momentomedya"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("contact", views.contactpage, name="contactpage"),
    path("references", views.referencespage, name="referencespage"),
    path("career", views.careerpage, name="careerpage")
]
