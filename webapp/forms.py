from django.forms import ModelForm, forms
from django import forms
from . import models

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        exclude = ["created_at"]
        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "description": forms.Textarea(attrs={"class":"form-control"}),
            "price": forms.TextInput(attrs={"class":"form-control", "type":"number"})

        }

class SelectProd(forms.Form):
    """sample frro:::"""
    prod_choices = [(i.pk, i.name) for i in models.Product.objects.all()]
    prod = forms.MultipleChoiceField(choices=prod_choices)

