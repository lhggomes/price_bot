from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django import forms
from django.urls import reverse_lazy
from pages.models import *


class Dashboard(TemplateView):
    template_name = 'base/dashboard.html'


class ManageProduct(CreateView):
    model = Product
    fields = ['code', 'description', 'ean', 'url', 'image_url']
    template_name = 'pages/dashboard/manage-product.html'
    success_url = reverse_lazy('manage-product')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)


class ManageCompany(CreateView):
    model = Company
    fields = ['description',]
    template_name = 'pages/dashboard/manage-company.html'
    success_url = reverse_lazy('manage-company')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)
