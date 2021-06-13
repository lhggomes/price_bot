from django.views.generic import TemplateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from pages.models import *
from price_bot.scraping import get_product


class Dashboard(TemplateView):
    template_name = 'pages/dashboard/main.html'


# Classes to manage the data
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
    fields = ['description', 'web_site', ]
    template_name = 'pages/dashboard/manage-company.html'
    success_url = reverse_lazy('manage-company')

    def get_context_data(self, **kwargs):
        # get_product()
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


# Classes to update the data
class UpdateProduct(UpdateView):
    model = Product
    fields = ['code', 'description', 'ean', 'url', 'image_url']
    template_name = 'pages/dashboard/update/update-view.html'
    success_url = reverse_lazy('update-product')

    def form_invalid(self, form):
        return super().form_invalid(form)


class UpdateCompany(UpdateView):
    model = Company
    fields = ['description', 'web_site', ]
    template_name = 'pages/dashboard/update/update-view.html'
    success_url = reverse_lazy('update-company')

    def form_invalid(self, form):
        return super().form_invalid(form)


class UpdateMinPrice(UpdateView):
    model = ProductMinValue
    fields = ['product', 'min_value', 'company']
    template_name = 'pages/dashboard/update/update-view.html'
    success_url = reverse_lazy('update-price')

    def form_invalid(self, form):
        return super().form_invalid(form)


class UpdateWebSiteDivs(UpdateView):
    model = WebSiteDivElement
    fields = ['price_div', 'ame_div', 'description_div', 'company']
    template_name = 'pages/dashboard/update/update-view.html'
    success_url = reverse_lazy('update-tech')

    def form_invalid(self, form):
        return super().form_invalid(form)


# Classes to delete the data
class DeleteProduct(DeleteView):
    model = Product
    template_name = 'pages/dashboard/update/delete-view.html'
    success_message = 'Produto excluído com sucesso!'
    success_url = reverse_lazy('manage-product')


class DeleteCompany(DeleteView):
    model = Company
    template_name = 'pages/dashboard/update/delete-view.html'
    success_message = 'Empresa excluído com sucesso!'
    success_url = reverse_lazy('manage-company')


class DeleteMinPrice(DeleteView):
    model = ProductMinValue
    template_name = 'pages/dashboard/update/delete-view.html'
    success_message = 'Valor excluído com sucesso!'
    success_url = reverse_lazy('manage-min-price')


class DeleteWebSiteDivs(DeleteView):
    model = WebSiteDivElement
    template_name = 'pages/dashboard/update/delete-view.html'
    success_message = 'Elemento excluído com sucesso!'
    success_url = reverse_lazy('manage-tech')


# Classes to generate the reports
class ReportProductPriceHistory(TemplateView):
    model = ProductPriceHistory
    template_name = 'pages/dashboard/report/product-history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price_history'] = ProductPriceHistory.objects.all()
        return context
