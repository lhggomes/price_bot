from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView
from django import forms
from django.urls import reverse_lazy
from pages.models import *


class Dashboard(TemplateView):
    template_name = 'pages/dashboard/main.html'


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
    fields = ['description', ]
    template_name = 'pages/dashboard/manage-company.html'
    success_url = reverse_lazy('manage-company')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)


class ManageMinPrice(CreateView):
    model = ProductMinValue
    fields = ['product', 'min_value', 'company']
    template_name = 'pages/dashboard/manage-min-price.html'
    success_url = reverse_lazy('manage-min-price')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["prices"] = ProductMinValue.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)


class ManageWebSiteDivs(CreateView):
    model = WebSiteDivElement
    fields = ['price_div', 'ame_div', 'description_div', 'company']
    template_name = 'pages/dashboard/manage-tech.html'
    success_url = reverse_lazy('manage-tech')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["div_elements"] = WebSiteDivElement.objects.all()
        return context

    def form_invalid(self, form):
        return super().form_invalid(form)
