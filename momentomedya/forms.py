from django import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm, widgets
from .models import CareerApply, RMAApply


class RMAForm(ModelForm):
    class Meta:
        model = RMAApply
        fields = "__all__"
        widgets = {
            'customer_first_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_last_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_company': forms.TextInput(attrs={'class':'form-control'}),
            'customer_email': forms.EmailInput(attrs={'class':'form-control'}),
            'customer_phone': forms.TextInput(attrs={'class':'form-control', 'placeholder': '+9...'}),
            'customer_address': forms.Textarea(attrs={'class':'form-control'}),
            'product_brand' : forms.TextInput(attrs={'class':'form-control'}),
            'product_model': forms.TextInput(attrs={'class':'form-control'}),
            'product_serial': forms.TextInput(attrs={'class':'form-control'}),
            'apply_topic': forms.Textarea(attrs={'class':'form-control'}),
            'problems': forms.CheckboxSelectMultiple(),
            'problem_note': forms.Textarea(attrs={'class':'form-control'}),
            #'other_checked': forms.Textarea(attrs={'class':'form-check-input', 'data-toggle':'modal', 'data-target':'#other_checked'}),
            #'pdpb_approval': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }


class CareerForm(ModelForm):
    class Meta:
        model = CareerApply
        fields = "__all__"
        widgets = {
            'inputName' : forms.TextInput(attrs={'class':'form-control'}),
            'inputSurname' : forms.TextInput(attrs={'class':'form-control'}),
            'inputEmail' : forms.EmailInput(attrs={'class':'form-control'}),
            'inputPhone' : forms.TextInput(attrs={'class':'form-control'}),
            'inputMessage' : forms.Textarea(attrs={'class':'form-control'}),
        }