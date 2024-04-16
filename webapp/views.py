from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView, FormView, TemplateView
from . import models
from . import forms
# Create your views here.


class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product_list"] = models.Product.objects.all()
        return context

class CreateProduct(FormView):
    template_name = "add_product.html"
    form_class = forms.ProductForm
    success_url = "/"


    def form_valid(self, form):
        print(form, "valid")
        data = form.cleaned_data
        print(data)
        models.Product.objects.create(
            **data

        )
        return super().form_valid(form)

    
class CreateBill(FormView):
    template_name = "sample_bill.html"
    form_class = forms.SelectProd
    success_url = "/"

    def form_valid(self, form):
        print(form.cleaned_data)
        data = form.cleaned_data
        prod = [int(i) for i in data["prod"]]
        sample_prod = models.Product.objects.filter(pk__in=prod)
        price = sum([i.price for i in sample_prod])
        print(price)
        return HttpResponseRedirect()

class BillView(TemplateView):
    template_name= "sample_bill.html"

    def get(self, *args, **kwargs):
        print(kwargs)
        return super().get(*args, **kwargs)
        