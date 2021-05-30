from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django import forms
from django.urls import reverse_lazy
from pages.models import *


class Dashboard(TemplateView):
    template_name = 'base/dashboard.html'


class CreateProduct(CreateView):
    model = Product
    fields = ['code', 'company', 'description', 'ean', 'url', 'image_url']
    template_name = 'pages/dashboard/create_prod.html'
    success_url = reverse_lazy('success-message')

